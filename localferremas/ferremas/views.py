from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout,authenticate,login as login_aut
from django.contrib.auth.models import User
from .models import *
from .forms import *
import requests
from rest_framework import viewsets, status
from .serializers import *

from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.decorators import api_view
from decimal import Decimal

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class TipoProductoViewset(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class ProductoOfertaViewset(viewsets.ModelViewSet):
    queryset = ProductoOferta.objects.all()
    serializer_class = ProductoOfertaSerializer

class CarritoViewset(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer


#### carrito
@action(detail=False, methods=['GET'])
def usuario_carrito(self, request):
        usuario = request.user
        carrito = Carrito.objects.filter(usuario=usuario)
        serializer = CarritoSerializer(carrito, many=True)
        return Response(serializer.data)


def carrito_de_compras(request):
    carrito = Carrito.objects.filter(usuario=request.user)

    # Obtener el valor del dólar desde la API del Mindicador
    response = requests.get('https://mindicador.cl/api/')
    data = response.json()
    valor_dolar = Decimal(str(data['dolar']['valor']))

    # Calcular el total del carrito en pesos chilenos
    total_carrito_pesos = 0
    for item in carrito:
        total_carrito_pesos += item.producto.precio * item.cantidad * valor_dolar

    # Si el usuario tiene descuento, calcularlo en pesos chilenos
    descuento = 0  # Calcula tu descuento aquí si lo necesitas
    descuento_pesos = descuento * valor_dolar

    # Calcular el subtotal y el total final en pesos chilenos
    subtotal_pesos = total_carrito_pesos - descuento_pesos
    total_final_pesos = subtotal_pesos

    context = {
        'carrito': carrito,
        'total_carrito_pesos': total_carrito_pesos,
        'subtotal_pesos': subtotal_pesos,
        'descuento_pesos': descuento_pesos,
        'total_final_pesos': total_final_pesos
    }

    return render(request, 'carrito.html', context)



@api_view(['POST'])
def agregar_al_carrito(request):
    if request.method == 'POST':
        producto_id = request.data.get('producto_id')
        try:
            producto = Producto.objects.get(pk=producto_id)
            usuario = request.user
            carrito_existente = Carrito.objects.filter(usuario=usuario, producto=producto).first()
            if carrito_existente:
                carrito_existente.cantidad += 1
                carrito_existente.save()
            else:
                carrito_nuevo = Carrito(usuario=usuario, producto=producto, cantidad=1)
                carrito_nuevo.save()
            # Decrementar el stock del producto
            producto.stock -= 1
            producto.save()
            return redirect('carrito_de_compras')
        except Producto.DoesNotExist:
            return Response({'error': 'El producto seleccionado no existe.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PATCH'])
def decrementar_cantidad_carrito(request, carrito_id):
    if request.method == 'PATCH':
        carrito = get_object_or_404(Carrito, pk=carrito_id)
        if carrito.cantidad > 1:
            carrito.cantidad -= 1
            carrito.save()
            # Incrementar el stock del producto
            carrito.producto.stock += 1
            carrito.producto.save()
            return Response({'mensaje': 'La cantidad del producto en el carrito ha sido decrementada.'})
        else:
            carrito.delete()
            # Incrementar el stock del producto
            carrito.producto.stock += 1
            carrito.producto.save()
            return Response({'mensaje': 'El producto ha sido eliminado del carrito.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def eliminar_del_carrito(request, carrito_id):
    if request.method == 'DELETE':
        carrito = get_object_or_404(Carrito, pk=carrito_id)
        # Obtener el producto del carrito antes de eliminarlo
        producto = carrito.producto
        carrito.delete()
        # Incrementar el stock del producto al eliminarlo del carrito
        producto.stock += carrito.cantidad
        producto.save()
        return Response({'mensaje': 'El producto ha sido eliminado del carrito.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
##########################


def index(request):
    response1 = requests.get('http://127.0.0.1:8000/api/productos/')
    response2 = requests.get('http://127.0.0.1:8000/api/Producto%20en%20oferta/')
    listado_productos = response1.json()
    listado_productos2 = response2.json()

    for producto in listado_productos:
        producto['en_oferta'] = False  

    for producto_oferta in listado_productos2:
        for producto in listado_productos:
            if producto['id'] == producto_oferta['producto']:
                producto['precio_oferta'] = producto_oferta['precio_oferta']
                producto['en_oferta'] = True


    context = {
        'listado': listado_productos,
    }

    return render(request, 'index.html', context)


def login(request):
    if request.POST:
        username =request.POST.get("username")
        password =request.POST.get("password")
        user= authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login_aut(request,user)
            return redirect(to="index")
    return render(request,'../templates/registration/login.html')

def register(request):
    if request.POST:
        username = request.POST.get("username")
        email = request.POST.get("email")
        number = request.POST.get("number")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat-password")

        user = User()

        user.set_password(password)
        user.username = username
        user.email = email
        user.number = number

        try:
            if password == repeat_password:
                user.save()
                return redirect(to="LOGIN")
            print()
        except:
            print()
    return render(request, '../templates/registration/register.html')



def productos(request):
    response = requests.get('http://127.0.0.1:8000/api/productos/')

    data = response.json()
    listado_productos = data


    context = {
        'listado': listado_productos,
            }

        
    return render(request, 'productos.html', context)
