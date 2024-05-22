from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout,authenticate,login as login_aut
from django.contrib.auth.models import User
from .models import CategoriaProducto, Producto, ProductoOferta, Carrito, CarritoItem
from django.contrib.auth.decorators import login_required, permission_required
import locale
from django.conf import settings
import mercadopago


# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.POST:
        username =request.POST.get("username")
        password =request.POST.get("password")
        user= authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login_aut(request,user)
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
    ofertas = ProductoOferta.objects.all()
    ctx = {
        "productos" : productos,
        "ofertas" : ofertas
    }
    return render(request, 'productos.html', ctx)

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
MERCADOPAGO_ACCESS_TOKEN = 'TEST-2707703782990962-052113-2fcbf2399d53397208c61d5f0cc6c38b-1821506213'

# MERCADO PAGO UWU
def checkout(request):
    usuario = request.user
    carrito = Carrito.objects.get(usuario=usuario)

    items = []
    for item in CarritoItem.objects.filter(carrito=carrito):
        items.append({
            "title": item.producto.nombre,
            "quantity": item.cantidad,
            "currency_id": "CLP",  # O la moneda que estés usando
            "unit_price": float(item.precio)
        })

    sdk = mercadopago.SDK(MERCADOPAGO_ACCESS_TOKEN)

    preference_data = {
        "items": items,
        "back_urls": {
            "success": 'http://127.0.0.1:8000/success',
            "failure": 'http://127.0.0.1:8000/failure',
            "pending": 'http://127.0.0.1:8000/pending'
        },
        "auto_return": "approved",
    }
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return render(request, "payments/checkout.html", {
        "preference_id": preference["id"]
    })



def success(request):
    return render(request, "payments/success.html")

def failure(request):
    return render(request, "payments/failure.html")

def pending(request):
    return render(request, "payments/pending.html")