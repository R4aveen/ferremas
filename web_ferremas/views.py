from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout,authenticate,login as auth_login
from django.contrib.auth.models import User
from .models import CategoriaProducto, Producto, ProductoOferta, Carrito, CarritoItem, Boleta, DetalleBoleta, TipoProducto, Pedido, DetallePedido
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
import locale
from django.conf import settings
# import mercadopago
from django.http import HttpResponseBadRequest, HttpResponse
from transbank.webpay.webpay_plus.transaction import Transaction
import random
from transbank.error.transbank_error import TransbankError
from django.core.paginator import Paginator
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.html import format_html, format_html_join
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
from .serializers import *
import requests
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid


# VIEWSETS
class TipoProductoViewset(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class CategoriaProductoViewset(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoOfertaViewset(viewsets.ModelViewSet):
    queryset = ProductoOferta.objects.all()
    serializer_class = ProductoOfertaSerializer

class CarritoViewset(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class BoletaViewset(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class DetalleBoletaViewset(viewsets.ModelViewSet):
    queryset = DetalleBoleta.objects.all()
    serializer_class = DetalleBoletaSerializer

class PedidoViewset(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

@api_view(['GET'])
def carrito_usuario(request, user_id):
    carrito = Carrito.objects.get(usuario_id=user_id)
    serializer = CarritoSerializer(carrito)
    return Response(serializer.data)

@api_view(['GET'])
def carrito_items_usuario(request, user_id):
    carrito = Carrito.objects.get(usuario_id=user_id)
    items = CarritoItem.objects.filter(carrito=carrito)
    serializer = CarritoItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pedido_usuario(request, user_id):
    carrito = Carrito.objects.get(usuario_id=user_id)
    pedido = Pedido.objects.filter(carrito=carrito).first()
    serializer = PedidoSerializer(pedido)
    return Response(serializer.data)




# VISTA VENDEDOR
# Verificar si el usuario es vendedor
def es_vendedor(user):
    return user.groups.filter(name='vendedor').exists()

@login_required
@user_passes_test(es_vendedor)
def ver_productos(request):
    productos_list = Producto.objects.all()
    ctx = {
        "productos" : productos_list
    }
    return render(request, 'trabajadores/vendedor/ver_productos.html', ctx)

@login_required
@user_passes_test(es_vendedor)
def gestionar_pedidos(request):
    pedidos = Pedido.objects.filter(estado='pendiente')
    return render(request, 'trabajadores/vendedor/gestionar_pedidos.html', {'pedidos': pedidos})

@login_required
def aprobar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    pedido.estado = 'pendiente de pago'
    pedido.payment_token = uuid.uuid4()  # Generar un nuevo token único
    pedido.save()

    # Enviar notificación al cliente
    current_site = get_current_site(request)
    pagar_url = request.build_absolute_uri(reverse('generar_boleta_webpay') + f'?token={pedido.payment_token}')

    # Crear el contenido de la tabla de productos
    carrito_items = CarritoItem.objects.filter(carrito=pedido.carrito)
    productos_html = format_html_join(
        '',
        '<tr>'
        '<td style="border: 1px solid #ddd; padding: 8px;">{}</td>'
        '<td style="border: 1px solid #ddd; padding: 8px;">{}</td>'
        '<td style="border: 1px solid #ddd; padding: 8px;">{}</td>'
        '</tr>',
        ((item.producto.nombre, item.cantidad, "{:.2f}".format(item.precio_total())) for item in carrito_items)
    )
    total = sum(item.precio_total() for item in carrito_items)

    mensaje = format_html(
        '<div style="font-family: Arial, sans-serif; color: #333; line-height: 1.5;">'
        '  <h2 style="color: #4CAF50;">Hola, {}</h2>'
        '  <p>Tu pedido con ID <strong>{}</strong> ha sido aprobado y está pendiente de pago.</p>'
        '  <p>Por favor, haz clic en el siguiente botón para realizar el pago:</p>'
        '  <a href="{}" style="display: inline-block; padding: 10px 20px; font-size: 16px; color: #fff; background-color: #28a745; text-decoration: none; border-radius: 5px; margin-top: 10px;">Realizar Pago</a>'
        '  <h3>Resumen del Pedido</h3>'
        '  <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">'
        '    <thead>'
        '      <tr>'
        '        <th style="border: 1px solid #ddd; padding: 8px; background-color: #333; color: #fff;">Producto</th>'
        '        <th style="border: 1px solid #ddd; padding: 8px; background-color: #333; color: #fff;">Cantidad</th>'
        '        <th style="border: 1px solid #ddd; padding: 8px; background-color: #333; color: #fff;">Subtotal</th>'
        '      </tr>'
        '    </thead>'
        '    <tbody>'
        '      {}'
        '    </tbody>'
        '    <tfoot>'
        '      <tr>'
        '        <td colspan="2" style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">Total</td>'
        '        <td style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">{}</td>'
        '      </tr>'
        '    </tfoot>'
        '  </table>'
        '  <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>'
        '  <p>Gracias por tu preferencia.</p>'
        '</div>',
        pedido.usuario.first_name, pedido.id, pagar_url, productos_html, total
    )

    send_mail(
        'Pedido Aprobado',
        '',  # Mensaje de texto plano vacío
        'pardodev78@gmail.com',
        [pedido.usuario.email],
        fail_silently=False,
        html_message=mensaje
    )

    messages.success(request, 'El pedido ha sido aprobado y está pendiente de pago. El cliente ha sido notificado.')
    return redirect('GESTIONAR_PEDIDOS')




@login_required
def rechazar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    usuario = pedido.usuario
    pedido_id = pedido.id

    # Enviar notificación al cliente
    send_mail(
        'Pedido Rechazado',
        f'Hola {usuario.first_name}, tu pedido con ID {pedido_id} ha sido rechazado.',
        'pardodev78@gmail.com',  # Reemplaza esto con tu dirección de correo
        [usuario.email],
        fail_silently=False,
    )
    
    # Borrar el pedido de la base de datos
    pedido.delete()
    
    messages.success(request, 'El pedido ha sido rechazado, el cliente ha sido notificado y el pedido ha sido eliminado.')
    return redirect('GESTIONAR_PEDIDOS')


@login_required
@user_passes_test(es_vendedor)
def enviar_orden(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    pedido.estado = 'preparando'
    pedido.save()
    # Aquí puedes agregar lógica adicional para notificar a los bodegueros
    return redirect('gestionar_pedidos')

@login_required
def realizar_pedido(request):
    carrito = Carrito.objects.get(usuario=request.user)
    
    # Verificar si ya existe un pedido pendiente o aprobado para este carrito
    pedido_existente = Pedido.objects.filter(carrito=carrito).exclude(estado__in=['cancelado', 'entregado']).first()
    
    if not pedido_existente:

        direccion_envio = request.user.direccion if hasattr(request.user, 'direccion') else 'Dirección no proporcionada'
        # Crear un nuevo pedido si no existe uno pendiente o aprobado
        pedido = Pedido.objects.create(
            usuario=request.user,
            carrito=carrito,
            estado='pendiente'
        )
        items = CarritoItem.objects.filter(carrito=carrito)
        for item in items:
            DetallePedido.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.precio,
                subtotal=item.precio_total()
            )
        carrito.pedido_aprobado = False
        carrito.save()
    
    return redirect('CARRITO')





@login_required
def anular_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    
    # Eliminar los detalles del pedido primero para evitar errores de clave foránea
    DetallePedido.objects.filter(pedido=pedido).delete()
    
    # Eliminar el pedido
    pedido.delete()

    carrito = pedido.carrito
    carrito.pedido_aprobado = False
    carrito.save()
    
    messages.success(request, 'Pedido anulado exitosamente.')
    return redirect('CARRITO')




# ============================================================================
# WEBPAY PLUS
# ============================================================================

def webpay_plus_commit(request):
    if request.method == 'GET':
        payment_token = request.GET.get("token")
        if not payment_token:
            return HttpResponseBadRequest("Token faltante en la URL.")

        try:
            # Verificar el token y obtener el pedido
            pedido = Pedido.objects.get(payment_token=payment_token, estado='pendiente de pago')
            user = pedido.usuario
            # Autenticar al usuario
            auth_login(request, user)

            token_ws = request.GET.get("token_ws")
            if not token_ws:
                return HttpResponseBadRequest("El parámetro 'token_ws' es requerido en la URL.")

            response = Transaction().commit(token=token_ws)
            productos = []
            precio_total = 0
            if response['status'] == 'AUTHORIZED':
                items_carrito = pedido.carrito.carritoitem_set.all()
                precio_total = sum(item.cantidad * item.producto.precio for item in items_carrito)

                if items_carrito.exists():
                    boleta = Boleta(usuario=user, total=precio_total)
                    boleta.save()

                    for item in items_carrito:
                        producto = item.producto
                        cantidad = item.cantidad
                        subtotal = cantidad * producto.precio
                        detalle = DetalleBoleta(boleta=boleta, producto=producto, cantidad=cantidad, subtotal=subtotal)
                        detalle.save()
                        productos.append({
                            'nombre': producto.nombre,
                            'cantidad': cantidad,
                            'subtotal': subtotal
                        })

                    pedido.carrito.carritoitem_set.all().delete()
                    pedido.estado = 'aprobado'
                    pedido.save()

            context = {
                'token': token_ws, 
                'response': response, 
                'productos': productos, 
                'total': precio_total,
                'pedido': pedido  # Añadir el pedido al contexto
            }
            return render(request, 'webpay/plus/commit.html', context)
        except Pedido.DoesNotExist:
            return HttpResponseBadRequest("Token inválido o pedido no encontrado.")
    elif request.method == 'POST':
        token = request.POST.get("token_ws")
        response = {"error": "Transacción con errores"}
        return render(request, 'webpay/plus/commit.html', {'token': token, 'response': response})








    

# INICIO TRANSACCION
def generarBoleta(request):
    if request.method == 'GET':
        try:
            pedido = Pedido.objects.get(usuario=request.user, estado='pendiente de pago')
            carrito = pedido.carrito
            items_carrito = carrito.carritoitem_set.all()
            if not items_carrito:
                return render(request, 'webpay/plus/error.html', {'error': 'El carrito está vacío'})

            precio_total = sum(item.cantidad * item.producto.precio for item in items_carrito)
            buy_order = str(random.randrange(1000000, 99999999))
            session_id = str(random.randrange(1000000, 99999999))
            return_url = request.build_absolute_uri(reverse('webpay_plus_commit') + f'?token={pedido.payment_token}')

            response = Transaction().create(buy_order, session_id, precio_total, return_url)
            return render(request, 'webpay/plus/create.html', {'response': response})
        except Pedido.DoesNotExist:
            messages.error(request, 'No se encontró un pedido pendiente de pago.')
            return redirect('CARRITO')
        except Exception as e:
            return render(request, 'webpay/plus/error.html', {'error': str(e)})
    else:
        return render(request, 'webpay/plus/error.html', {'error': 'Método HTTP no permitido'})





    
# ERROR EN LA TRANSACCION
def webpay_plus_commit_error(request):
    return HttpResponse("Error en la transacción de pago")

# 
def webpay_plus_refund(request):
    if request.method == 'POST':
        token = request.POST.get("token_ws")
        amount = request.POST.get("amount")

        try:
            response = Transaction().refund(token, amount)
            return render(request, "webpay/plus/refund.html", {'token': token, 'amount': amount, 'response': response})
        except TransbankError as e:
            return render(request, 'webpay/plus/error.html', {'error': str(e)})
        
# 
def webpay_plus_refund_form(request):
    return render(request, 'webpay/plus/refund-form.html')

#

#
def status(request):
    token_ws = request.POST.get('token_ws')
    tx = Transaction()
    resp = tx.status(token_ws)
    return render(request, 'webpay/plus/status.html', {'response': resp, 'token': token_ws, 'req': request.POST})

#
def show_create(request):
    return render(request, 'webpay/plus/status-form.html')

#
def webpay_plus_create(request):
    if request.method == 'GET':
        buy_order = str(random.randrange(1000000, 99999999))
        session_id = str(random.randrange(1000000, 99999999))
        amount = random.randrange(10000, 1000000)
        return_url = request.build_absolute_uri('/webpay-plus/commit')

        response = Transaction().create(buy_order, session_id, amount, return_url)
        return render(request, 'webpay/plus/create.html', {'response': response})

# ============================================================================




# Create your views here.
def base(request):
    grupos_usuario = request.user.groups.values_list('name', flat=True)
    ctx = {
        'es_vendedor': 'vendedor' in grupos_usuario,
        'es_contador': 'contador' in grupos_usuario,
        'es_bodeguero': 'bodeguero' in grupos_usuario,
        'es_despachador': 'despachador' in grupos_usuario,
        'es_cliente': 'cliente' in grupos_usuario,
    }
    return render(request, 'base.html', ctx)




def login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            if user.groups.filter(name='cliente').exists():
                return redirect(to="PRODUCTOS")
            elif user.groups.filter(name='vendedor').exists():
                return redirect(to="ver_productos")
            elif user.groups.filter(name='bodeguero').exists():
                return redirect(to="ver_pedidos")
            elif user.groups.filter(name='contador').exists():
                return redirect(to="contador")
            return redirect(to="INDEX")
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect(to="INDEX")

def registro(request):
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
                cliente_group = Group.objects.get(name='cliente')
                user.groups.add(cliente_group)
                return redirect(to="LOGIN")
            print()
        except:
            print()
    return render(request, 'registro.html')

def productos(request):
    response_productos = requests.get('http://127.0.0.1:8000/api/productos/')
    response_categorias = requests.get('http://127.0.0.1:8000/api/categorias_producto/')
    response_tipos = requests.get('http://127.0.0.1:8000/api/tipos_producto/')
    response_productos_oferta = requests.get('http://127.0.0.1:8000/api/producto_oferta/')

    data_productos = response_productos.json()
    data_categorias = response_categorias.json()
    data_tipos = response_tipos.json()
    data_productos_oferta = response_productos_oferta.json()

    listado_productos = data_productos
    listado_categorias = data_categorias
    listado_tipos = data_tipos
    listado_productos_oferta = data_productos_oferta



    paginator = Paginator(listado_productos, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        "page_obj": page_obj,
        "productos" : listado_productos,
        "categorias": listado_categorias,
        "ofertas" : listado_productos_oferta,
        "tipos": listado_tipos,

    }
    return render(request, 'productos.html', ctx)

def categoriaprod(request, categoriaprod_id):
    categoria = get_object_or_404(CategoriaProducto, id=categoriaprod_id)
    categorias_list = CategoriaProducto.objects.all()

    tipos_list = TipoProducto.objects.all()

    productos = Producto.objects.filter(categoria=categoria)
    paginator = Paginator(productos, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        "page_obj": page_obj,
        "categoria": categoria,
        "categorias": categorias_list,
        "tipos": tipos_list,


    }
    return render(request, "categoria_prod.html", ctx)

def tipoprod(request, tipoprod_id):
    tipo = get_object_or_404(TipoProducto, id=tipoprod_id)
    tipos_list = TipoProducto.objects.all()

    categorias_list = CategoriaProducto.objects.all()

    productos = Producto.objects.filter(tipo=tipo)
    paginator = Paginator(productos, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        "page_obj": page_obj,
        "tipo": tipo,
        "tipos": tipos_list,
        "categorias": categorias_list,


    }
    return render(request, "tipo_prod.html", ctx)



### carrito
from decimal import Decimal
from django.utils.formats import number_format

@login_required(login_url='/login/')
def carrito(request):
    # Obtener el valor actual del dólar
    response_dolar = requests.get('https://mindicador.cl/api/dolar')
    data_dolar = response_dolar.json()
    valor_dolar = Decimal(data_dolar['serie'][0]['valor'])

    # Usar get_or_create para manejar el caso en que no existe un carrito
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    items_carrito = CarritoItem.objects.filter(carrito=carrito)
    # Convertir los precios de los productos a CLP y calcular el subtotal
    for item in items_carrito:
        item.precio = round(item.producto.precio * valor_dolar)  # Precio en CLP redondeado
        item.subtotal = item.precio * item.cantidad  # Subtotal en CLP
        item.save()

    total = sum(item.subtotal for item in items_carrito)
    iva = total * Decimal('0.19')  # Calcular el IVA del 19%
    total_con_iva = total + iva  # Total con IVA incluido
    
    for item in items_carrito:
        item.precio = round(item.producto.precio * valor_dolar)  # Precio en CLP redondeado
        item.subtotal = item.precio * item.cantidad  # Subtotal en CLP
        item.save()
    # Formatear los valores para la plantilla
    total_formato = number_format(total, decimal_pos=0, use_l10n=True)
    iva_formato = number_format(iva, decimal_pos=0, use_l10n=True)
    total_con_iva_formato = number_format(total_con_iva, decimal_pos=0, use_l10n=True)
    for item in items_carrito:
        item.subtotal_formato = number_format(item.subtotal, decimal_pos=0, use_l10n=True)
        item.precio_formato = number_format(item.precio, decimal_pos=0, use_l10n=True)

    pedido = Pedido.objects.filter(carrito=carrito).first()
    pedido_aprobado = pedido and pedido.estado == 'aprobado'

    return render(request, 'carrito.html', {
        'items_carrito': items_carrito,
        'total_formato': total_formato,
        'iva_formato': iva_formato,
        'total_con_iva_formato': total_con_iva_formato,
        'carrito': carrito,
        'pedido_aprobado': pedido_aprobado,
        'pedido': pedido,
    })


from django.contrib import messages

# METODOS DEL CARRITO
@login_required(login_url='/login/')
def agregar_al_carrito(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    
    if producto.stock > 0:  # Verificar que haya stock disponible
        carrito = Carrito.objects.get_or_create(usuario=request.user)[0]
        item_existente = carrito.carritoitem_set.filter(producto=producto).first()
        
        if item_existente:
            # Si el producto ya está en el carrito, aumenta la cantidad
            item_existente.cantidad += 1
            item_existente.save()
        else:
            # Si el producto no está en el carrito, crea un nuevo ítem
            CarritoItem.objects.create(carrito=carrito, producto=producto, precio=producto.precio)
        
        # Restar el stock del producto
        producto.stock -= 1
        producto.save()
    else:
        # Manejar el caso en que no haya suficiente stock
        messages.error(request, 'No hay suficiente stock disponible para este producto.')
    
    return redirect('PRODUCTOS')


@login_required(login_url='/login/')
def eliminar_del_carrito(request, id_item):
    item = CarritoItem.objects.get(pk=id_item)
    item.delete()
    return redirect('CARRITO')

@login_required(login_url='/login/')
def vaciar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    carrito.carritoitem_set.all().delete()
    return redirect('CARRITO')

# MAS METODOS
@login_required(login_url='/login/')
def aumentar_cantidad(request, id_item):
    item = get_object_or_404(CarritoItem, pk=id_item)
    item.cantidad += 1
    item.save()
    return redirect('CARRITO')

@login_required(login_url='/login/')
def disminuir_cantidad(request, id_item):
    item = get_object_or_404(CarritoItem, pk=id_item)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()
    return redirect('CARRITO')


@login_required
def perfil_usuario(request):
    usuario = get_object_or_404(User, pk=request.user.pk)
    boletas = Boleta.objects.filter(usuario=usuario)
    detalles_boletas = DetalleBoleta.objects.filter(boleta__in=boletas)
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-creado_en')
    for pedido in pedidos:
        pedido.items = DetallePedido.objects.filter(pedido=pedido)

    context = {
        'usuario': usuario,
        'boletas': boletas,
        'detalles_boletas': detalles_boletas,
        'pedidos': pedidos,  # Añadir pedidos al contexto
    }
    return render(request, 'perfil_usuario.html', context)


@login_required
def actualizar_perfil(request):
    usuario = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        usuario.first_name = request.POST['nombre']
        usuario.last_name = request.POST['apellidos']
        usuario.email = request.POST['correo']
        usuario.direccion = request.POST['direccion']
        usuario.save()
        messages.success(request, 'Perfil actualizado exitosamente')
        return redirect('PERFIL_USUARIO')
    else:
        messages.error(request, 'Error al actualizar el perfil')
        return redirect('PERFIL_USUARIO')



@login_required
def generar_boleta(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items_carrito = CarritoItem.objects.filter(carrito=carrito)
    total = sum(item.precio_total() for item in items_carrito)

    if not carrito.pedido_aprobado:
        messages.error(request, "Tu pedido aún no ha sido aprobado.")
        return redirect('CARRITO')

    boleta = Boleta.objects.create(
        usuario=request.user,
        total=total,
    )

    for item in items_carrito:
        DetalleBoleta.objects.create(
            boleta=boleta,
            producto=item.producto,
            cantidad=item.cantidad,
            subtotal=item.precio_total(),
        )

    carrito.carritoitem_set.all().delete()
    carrito.pedido_aprobado = False
    carrito.save()

    # Notificar al cliente sobre el estado del pedido
    send_mail(
        'Pedido Completado',
        'Tu pedido ha sido pagado y está en preparación.',
        'pardodev78@gmail.com',
        [request.user.email],
        fail_silently=False,
    )

    return redirect('CARRITO')

# Bodeguero

def es_bodeguero(user):
    return user.groups.filter(name='bodeguero').exists()


@login_required
@user_passes_test(es_bodeguero)
def ver_pedidos(request):
    pedidos = Pedido.objects.filter(Q(estado='aprobado') | Q(estado='preparando'))
    return render(request, 'trabajadores/bodeguero/ver_pedidos.html', {'pedidos': pedidos})

@login_required
@user_passes_test(es_bodeguero)
def aceptar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido.estado = 'preparando'
    pedido.save()

    # Notificar al cliente que el pedido está en preparación
    mensaje_html = format_html(
        '<div style="font-family: Arial, sans-serif; color: #333; line-height: 1.5;">'
        '  <h2 style="color: #4CAF50;">Hola, {}</h2>'
        '  <p>Tu pedido está siendo preparado.</p>'
        '  <p>Te notificaremos una vez que esté listo para el envío.</p>'
        '  <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>'
        '  <p>Gracias por tu preferencia.</p>'
        '</div>',
        pedido.usuario.first_name
    )

    send_mail(
        'Pedido en Preparación',
        '',  # Mensaje de texto plano vacío
        'pardodev78@gmail.com',  # Cambia esto por tu dirección de correo
        [pedido.usuario.email],
        fail_silently=False,
        html_message=mensaje_html
    )

    messages.success(request, 'El pedido está en preparación.')
    return redirect('ver_pedidos')

@login_required
@user_passes_test(es_bodeguero)
def entregar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido.estado = 'enviado'
    pedido.save()

    # Notificar al cliente que el pedido ha sido enviado
    mensaje_html = format_html(
        '<div style="font-family: Arial, sans-serif; color: #333; line-height: 1.5;">'
        '  <h2 style="color: #4CAF50;">Hola, {}</h2>'
        '  <p>Tu pedido  ha sido enviado.</p>'
        '  <p>Te notificaremos una vez que esté en camino a tu dirección de envío.</p>'
        '  <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>'
        '  <p>Gracias por tu preferencia.</p>'
        '</div>',
        pedido.usuario.first_name
    )

    send_mail(
        'Pedido Enviado',
        '',  # Mensaje de texto plano vacío
        'pardodev78@gmail.com',  # Cambia esto por tu dirección de correo
        [pedido.usuario.email],
        fail_silently=False,
        html_message=mensaje_html
    )

    messages.success(request, 'El pedido ha sido enviado.')
    return redirect('ver_pedidos')



# Despachador
def es_despachador(user):
    return user.groups.filter(name='despachador').exists()

@login_required
@user_passes_test(es_despachador)
def ver_pedidos_despachador(request):
    pedidos = Pedido.objects.filter(estado='enviado')
    return render(request, 'trabajadores/despachador/ver_pedidos.html', {'pedidos': pedidos})


@login_required
@user_passes_test(es_despachador)
def entregar_pedido_despachador(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido.estado = 'entregado'
    pedido.hora_entrega = timezone.now()  # Guardar la hora actual de entrega
    pedido.save()

    # Formatear la hora de entrega
    hora_entrega = pedido.hora_entrega.strftime('%Y-%m-%d %H:%M:%S')

    # Notificar al cliente que el pedido ha sido entregado
    mensaje_html = format_html(
        '<div style="font-family: Arial, sans-serif; color: #333; line-height: 1.5;">'
        '  <h2 style="color: #4CAF50;">Hola, {}</h2>'
        '  <p>Tu pedido ha sido entregado.</p>'
        '  <p>La entrega se realizó el <strong>{}</strong>.</p>'
        '  <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>'
        '  <p>Gracias por tu preferencia.</p>'
        '</div>',
        pedido.usuario.first_name, hora_entrega
    )

    send_mail(
        'Pedido Entregado',
        '',  # Mensaje de texto plano vacío
        'pardodev78@gmail.com',  # Cambia esto por tu dirección de correo
        [pedido.usuario.email],
        fail_silently=False,
        html_message=mensaje_html
    )

    # Eliminar los detalles del pedido primero para evitar errores de clave foránea
    DetallePedido.objects.filter(pedido=pedido).delete()

    # Eliminar el pedido
    pedido.delete()

    messages.success(request, 'El pedido ha sido entregado y eliminado del sistema.')
    return redirect('ver_pedidos_despachador')

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.units import inch

def generar_pdf_transaccion(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="transaccion_{pedido_id}.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Adjusted Title Position
    p.setFont("Helvetica-Bold", 16)
    p.drawString(1 * inch, 10.3 * inch, "Resultado de Transacción")
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 9.9 * inch, f"ID del Pedido: {pedido_id}")
    p.drawString(1 * inch, 9.6 * inch, f"Status: {pedido.estado}")
    
    # Line
    p.setLineWidth(0.5)
    p.line(1 * inch, 9.4 * inch, 7.5 * inch, 9.4 * inch)

    # Table Header
    p.setFont("Helvetica-Bold", 12)
    p.drawString(1 * inch, 9.2 * inch, "Productos:")
    
    p.setFont("Helvetica-Bold", 10)
    p.drawString(1 * inch, 8.9 * inch, "Producto")
    p.drawString(3 * inch, 8.9 * inch, "Cantidad")
    p.drawString(4 * inch, 8.9 * inch, "Subtotal")

    # Table Content
    y = 8.6 * inch
    p.setFont("Helvetica", 10)
    for item in DetallePedido.objects.filter(pedido=pedido):
        p.drawString(1 * inch, y, f"{item.producto.nombre}")
        p.drawString(3 * inch, y, f"{item.cantidad}")
        p.drawString(4 * inch, y, f"${item.subtotal:.2f}")
        y -= 0.3 * inch
        if y < 1 * inch:  # New page if too many items
            p.showPage()
            p.setFont("Helvetica", 10)
            y = 10 * inch

    # Total
    p.setFont("Helvetica-Bold", 10)
    p.drawString(1 * inch, y, "Total")
    p.drawString(4 * inch, y, f"${sum(item.subtotal for item in DetallePedido.objects.filter(pedido=pedido)):.2f}")

    

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response






























































































































































































































































































##### basti basti jsajajsa


import random

def index(request):
    productos_oferta = Producto.objects.filter(en_oferta=True).order_by('?')[:3]
    categorias_random = CategoriaProducto.objects.order_by('?')[:3]
    
    ctx = {
        'productos_oferta': productos_oferta,
        'categorias_random': categorias_random,
    }
    return render(request, 'index.html', ctx)
