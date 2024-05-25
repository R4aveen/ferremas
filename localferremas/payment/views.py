# En tu archivo views.py

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import random
from datetime import datetime
from .models import Pago
from .serializers import PagoPostSerializer, TransaccionPostSerializer
from ferremas.models import Pedido
from rest_framework.exceptions import ValidationError


def payment(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    
    # Comprobar si existe un pago para el pedido
    if Pago.objects.filter(pedido=pedido).exists():
        return HttpResponse('Este pedido ya tiene un pago asociado.', status=400)

    # Preparar los parámetros para la API
    params = {
        "buy_order": str(pedido.id),
        "session_id": str(random.randint(100000, 999999)),
        "amount": pedido.total,
        "return_url": "http://127.0.0.1:8000/verify_transaction"
    }
    
    headers = {
        "Tbk-Api-Key-Id": "597055555532",
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type": "application/json"
    }

    # Hacer la llamada a la API
    response = requests.post('https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions', headers=headers, json=params)

    # Si la respuesta es exitosa, obtener el token y renderizar la página de pago
    if response.status_code == 200:
        token = response.json()['token']
        return render(request, 'payment.html', {'token': token, 'message': 'Proceder al pago', 'submit': 'Pagar'})
    else:
        print(response.text)
        return HttpResponse(status=400)

@csrf_exempt
def verify_transaction(request):
    if request.method == 'POST':
        response = request.POST

        return render(request, 'response.html', {'response': response})
    elif request.method == 'GET':
        # Capturar el token de la URL
        token = request.GET.get('token_ws')

        url = f"https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{token}"
        headers = {
            "Tbk-Api-Key-Id": "597055555532",
            "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
            
            "Content-Type": "application/json"
        }
        
        response = requests.put(url, headers=headers)
        
        # Crear un pago
        response_data = response.json()
        pago_data = {
            'pedido': response_data['buy_order'],
            'metodo_pago': response_data['payment_type_code'],
            'monto': response_data['amount'],
            'estado_pago': response_data['response_code'],
            'fecha' : datetime.strptime(response_data['transaction_date'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
        }
        serializer = PagoPostSerializer(data=pago_data)
        if serializer.is_valid():
            pago = serializer.save()
        else:
            return HttpResponse(serializer.errors, status=400)

        # Crear la transacción
        transaccion_data = {
            'pedido': pago.pedido.id,
            'cliente': pago.pedido.usuario.id,
            'pago': pago.id,
        }
        transaccion_serializer = TransaccionPostSerializer(data=transaccion_data)
        if transaccion_serializer.is_valid():
            transaccion_serializer.save()
        else:
            raise ValidationError(transaccion_serializer.errors)
        
        return render(request, 'response.html', {'response': 'Pago exitoso.'})
    else:
        return HttpResponseBadRequest("Método no permitido")
