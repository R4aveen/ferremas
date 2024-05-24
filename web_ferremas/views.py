from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout,authenticate,login as login_aut
from django.contrib.auth.models import User
from .models import CategoriaProducto, Producto, ProductoOferta, Carrito, CarritoItem, Boleta, DetalleBoleta, TipoProducto
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
import locale
from django.conf import settings
# import mercadopago
from django.http import HttpResponseBadRequest, HttpResponse
from transbank.webpay.webpay_plus.transaction import Transaction
import random
from transbank.error.transbank_error import TransbankError
from django.core.paginator import Paginator


# ============================================================================
# WEBPAY PLUS
# ============================================================================
def webpay_plus_commit(request):
    if request.method == 'GET':
        token = request.GET.get("token_ws")
        if token is None:
            return HttpResponseBadRequest("El parámetro 'token_ws' es requerido en la URL.")

        response = Transaction().commit(token=token)
        productos = []
        precio_total = 0
        if response['status'] == 'AUTHORIZED':
            carrito = Carrito.objects.get(usuario=request.user)
            items_carrito = carrito.carritoitem_set.all()
            precio_total = sum(item.cantidad * item.producto.precio for item in items_carrito)

            boleta = Boleta(total=precio_total)
            boleta.save()

            for item in items_carrito:
                producto = item.producto
                cantidad = item.cantidad
                subtotal = cantidad * producto.precio
                detalle = DetalleBoleta(boleta=boleta, producto=producto, cantidad=cantidad, subtotal=subtotal)
                detalle.save()
                # Agregar un diccionario con información del producto a la lista de productos
                productos.append({
                    'nombre': producto.nombre,
                    'cantidad': cantidad,
                    'subtotal': subtotal
                })

            carrito.carritoitem_set.all().delete()

        context = {'token': token, 'response': response, 'productos': productos, 'total': precio_total}
        return render(request, 'webpay/plus/commit.html', context)
    elif request.method == 'POST':
        token = request.POST.get("token_ws")
        response = {"error": "Transacción con errores"}
        return render(request, 'webpay/plus/commit.html', {'token': token, 'response': response})

    

# INICIO TRANSACCION
def generarBoleta(request):
    if request.method == 'GET':
        carrito = Carrito.objects.get_or_create(usuario=request.user)[0]
        items_carrito = carrito.carritoitem_set.all()
        if not items_carrito:
            return render(request, 'webpay/plus/error.html', {'error': 'El carrito está vacío'})

        precio_total = sum(item.cantidad * item.producto.precio for item in items_carrito)
        buy_order = str(random.randrange(1000000, 99999999))
        session_id = str(random.randrange(1000000, 99999999))
        return_url = request.build_absolute_uri('/webpay-plus/commit')

        try:
            response = Transaction().create(buy_order, session_id, precio_total, return_url)
            return render(request, 'webpay/plus/create.html', {'response': response})
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
def webpay_plus_refund_form(request):
    return render(request, 'webpay/plus/refund-form.html')

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
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login_aut(request, user)
            if user.groups.filter(name='vendedor').exists():
                return redirect(to="vendedor")
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
                return redirect(to="LOGIN")
            print()
        except:
            print()
    return render(request, 'registro.html')

def productos(request):
    productos = Producto.objects.all()

    categorias_list = CategoriaProducto.objects.all()

    tipos_list = TipoProducto.objects.all()

    ofertas = ProductoOferta.objects.all()
    paginator = Paginator(productos, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        "page_obj": page_obj,
        "productos" : productos,
        "categorias": categorias_list,
        "ofertas" : ofertas,
        "tipos": tipos_list,

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

def is_vendedor(user):
    return user.groups.filter(name='vendedor').exists()

@user_passes_test(is_vendedor, login_url='/login/')
def vendedor(request):
    productos_list = Producto.objects.all()
    categorias_list = CategoriaProducto.objects.all()
    paginator = Paginator(productos_list, 6) 
    tipos_list = TipoProducto.objects.all()


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        "page_obj": page_obj,
        "categorias": categorias_list,
        "tipos": tipos_list,

    }
    return render(request, "trabajadores/vendedor/vendedor.html", ctx)

@user_passes_test(is_vendedor, login_url='/login/')
def categoria(request, categoria_id):
    categoria = get_object_or_404(CategoriaProducto, id=categoria_id)
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
    return render(request, "trabajadores/vendedor/categoria.html", ctx)

@user_passes_test(is_vendedor, login_url='/login/')
def tipo(request, tipo_id):
    tipo = get_object_or_404(TipoProducto, id=tipo_id)
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
    return render(request, "trabajadores/vendedor/tipo.html", ctx)





def crud_productos(request):
    return render(request, 'crud_productos.html')


### carrito
@login_required(login_url='/login/')
def carrito(request):

    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

    carrito = Carrito.objects.get_or_create(usuario=request.user)[0]
    items_carrito = carrito.carritoitem_set.all()
    sub_total_items = sum(item.cantidad * item.producto.precio for item in items_carrito)
    total = sum(item.precio_total() for item in items_carrito)
    total_formateado = locale.format_string("%d", total, grouping=True)



    ctx = {
        'items_carrito': items_carrito,
        'total': total,
        'total_formato': total_formateado,
        'sub_total':sub_total_items
        }
    return render(request, 'carrito.html', ctx)

# METODOS DEL CARRITO
@login_required(login_url='/login/')
def agregar_al_carrito(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    carrito = Carrito.objects.get_or_create(usuario=request.user)[0]
    item_existente = carrito.carritoitem_set.filter(producto=producto).first()
    
    if item_existente:
        # Si el producto ya está en el carrito, aumenta la cantidad
        item_existente.cantidad += 1
        item_existente.save()
    else:
        # Si el producto no está en el carrito, crea un nuevo ítem
        CarritoItem.objects.create(carrito=carrito, producto=producto, precio=producto.precio)
        
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

### fin carrito
# MERCADOPAGO_ACCESS_TOKEN = 'TEST-2707703782990962-052210-1c16fe9d61ba257bc74b01bf7721ba4a-1821506213'

# MERCADO PAGO UWU
# @login_required(login_url='/login/')  # Asegura que el usuario esté autenticado
# def checkout(request):
#     usuario = request.user
#     try:
#         carrito = Carrito.objects.get(usuario=usuario)
#     except Carrito.DoesNotExist:
#         # Maneja el caso en que el carrito no existe para el usuario
#         return redirect('CARRITO')

#     items = []
#     for item in CarritoItem.objects.filter(carrito=carrito):
#         items.append({
#             "title": item.producto.nombre,
#             "quantity": item.cantidad,
#             "currency_id": "CLP",  # Ajusta según la moneda que estés utilizando
#             "unit_price": float(item.producto.precio)  # Utiliza el precio del producto
#         })

#     sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

#     try:
#         preference_data = {
#             "items": items,
#             "back_urls": {
#                 "success": 'http://127.0.0.1:8000/success/',
#                 "failure": 'http://127.0.0.1:8000/failure/',
#                 "pending": 'http://127.0.0.1:8000/pending/'
#             },
#             "auto_return": "approved",
#         }
#         preference_response = sdk.preference().create(preference_data)
#         preference = preference_response["response"]

#         return render(request, "payments/checkout.html", {
#             "preference_id": preference["id"]
#         })
#     except Exception as e:
#         # Maneja el error de manera adecuada, puede ser un log, redirección a una página de error, etc.
#         print("Error al crear la preferencia de pago:", e)
#         return redirect('CARRITO')


# def success(request):
#     return render(request, "payments/success.html")

# def failure(request):
#     return render(request, "payments/failure.html")

# def pending(request):
#     return render(request, "payments/pending.html")