import pytest
from .models import *
from .forms import *
from django.db import IntegrityError
from django.contrib.auth.models import User
# =======================================================================
# CATEGORIA
# =======================================================================
@pytest.mark.django_db
def test_crear_categoria_producto():
    categoria_producto = CategoriaProducto.objects.create(
        categoria="Gasfiteria"
    )
    assert categoria_producto.categoria == "Gasfiteria"
    assert str(categoria_producto) == "Gasfiteria"

# TESTING ERROR
@pytest.mark.django_db
def test_crear_categoria_producto_con_categoria_vacia():
    with pytest.raises(ValidationError):
        categoria_producto = CategoriaProducto(categoria="")
        categoria_producto.full_clean()

# =======================================================================
# TIPO CATEGORIA
# =======================================================================
@pytest.mark.django_db
def test_crear_tipo_producto():
    tipo_producto = TipoProducto.objects.create(
        tipo = "Lubricante"
    )
    assert tipo_producto.tipo == "Lubricante"
    assert str(tipo_producto) == "Lubricante"

# TIPO CATEGORIA SIN CATEGORIA
@pytest.mark.django_db
def test_crear_categoria_producto_con_categoria_vacia():
    with pytest.raises(ValidationError):
        categoria_producto = CategoriaProducto(categoria="")
        categoria_producto.full_clean()

# =======================================================================
# CREAR PRODUCTO
# =======================================================================

@pytest.mark.django_db
def test_crear_producto():
    categoria_producto = CategoriaProducto.objects.create(
        categoria="Gasfiteria"
    )
    tipo_producto = TipoProducto.objects.create(
        tipo = "Lubricante"
    )

    producto = Producto.objects.create(
        nombre = "Cierra electrica",
        precio = 5990,
        stock = 55,
        descripcion = "Cierra de buena calidad",
        en_oferta = False
    )
    producto.categoria.set({categoria_producto})
    producto.tipo.set({tipo_producto})
    assert producto.nombre == "Cierra electrica"
    assert producto.precio == 5990
    assert producto.stock == 55
    assert producto.descripcion == "Cierra de buena calidad"
    assert categoria_producto in producto.categoria.all()
    assert tipo_producto in producto.tipo.all()
    assert producto.en_oferta == False

    assert str(producto) == "Cierra electrica"

# TEST PRODUCTO SIN NOMBRE,PRECIO NEGATIVO Y STOCK NEGATIVO
@pytest.mark.django_db
def test_crear_producto_sin_nombre_precio_stock():
    categoria_producto = CategoriaProducto.objects.create(
        categoria="Gasfiteria"
    )
    tipo_producto = TipoProducto.objects.create(
        tipo="Lubricante"
    )

    with pytest.raises(ValidationError):
        producto = Producto.objects.create(
            descripcion="Cierra de buena calidad",
            en_oferta=False
        )
        producto.categoria.set([categoria_producto])
        producto.tipo.set([tipo_producto])
        producto.full_clean()

# =======================================================================
# TEST CREAR OFERTA
# =======================================================================
@pytest.mark.django_db
def test_crear_oferta():
    categoria_producto = CategoriaProducto.objects.create(
        categoria="Gasfiteria"
    )
    tipo_producto = TipoProducto.objects.create(
        tipo = "Lubricante"
    )

    productos = Producto.objects.create(
        nombre = "Cierra electrica",
        precio = 5990,
        stock = 55,
        descripcion = "Cierra de buena calidad",
        en_oferta = False
    )
    productos.categoria.set({categoria_producto})
    productos.tipo.set({tipo_producto})

    oferta = ProductoOferta.objects.create(
        producto = productos,
        precio_oferta = 10990
    )

    
    assert productos.nombre == "Cierra electrica"
    assert productos.precio == 5990
    assert productos.stock == 55
    assert productos.descripcion == "Cierra de buena calidad"
    assert categoria_producto in productos.categoria.all()
    assert tipo_producto in productos.tipo.all()
    assert productos.en_oferta == False

    assert oferta.producto == productos
    assert oferta.precio_oferta == 10990
    assert oferta.producto.nombre == "Cierra electrica"

# TEST CREAR OFERTA SIN PRODUCTO
@pytest.mark.django_db
def test_crear_oferta_sin_producto():
    with pytest.raises(ValidationError):
        ProductoOferta.objects.create(
            precio_oferta=10990
        )

# =======================================================================
# TEST CREAR CARRITO
# =======================================================================
    
@pytest.mark.django_db
def test_crear_carrito():
    usuario = User.objects.create_user(username='testuser', password='12345')
    carrito = Carrito.objects.create(usuario=usuario)
    
    assert carrito.usuario == usuario
    assert carrito.pedido_aprobado == False
    assert str(carrito) == f"{usuario} - {carrito.creado_en}"

@pytest.mark.django_db
def test_crear_carrito_sin_usuario():
    with pytest.raises(ValidationError):
        Carrito.objects.create(pedido_aprobado=False)

# =======================================================================
# TEST CREAR CARRITO ITEM
# =======================================================================

@pytest.mark.django_db
def test_crear_carrito_item():
    usuario = User.objects.create_user(username='testuser', password='12345')
    categoria_producto = CategoriaProducto.objects.create(categoria="Gasfiteria")
    tipo_producto = TipoProducto.objects.create(tipo="Lubricante")
    producto = Producto.objects.create(nombre="Cierra electrica", precio=5990, stock=55, descripcion="Cierra de buena calidad")
    producto.categoria.set([categoria_producto])
    producto.tipo.set([tipo_producto])
    carrito = Carrito.objects.create(usuario=usuario)
    carrito_item = CarritoItem.objects.create(carrito=carrito, producto=producto, cantidad=2, precio=5990)
    
    assert carrito_item.carrito == carrito
    assert carrito_item.producto == producto
    assert carrito_item.cantidad == 2
    assert carrito_item.precio == 5990
    assert carrito_item.precio_total() == 2 * 5990

# SIN ESPECIICAR NINGUN CAMPO; SIN ESPECIGICAR CANTIDAD Y PRECIO
@pytest.mark.django_db
def test_crear_carrito_item_sin_campos():
    usuario = User.objects.create_user(username='testuser', password='12345')
    categoria_producto = CategoriaProducto.objects.create(categoria="Gasfiteria")
    tipo_producto = TipoProducto.objects.create(tipo="Lubricante")
    producto = Producto.objects.create(nombre="Cierra electrica", precio=5990, stock=55, descripcion="Cierra de buena calidad")
    producto.categoria.set([categoria_producto])
    producto.tipo.set([tipo_producto])
    carrito = Carrito.objects.create(usuario=usuario)
    
    # Intentamos crear un CarritoItem sin especificar todos los campos requeridos
    with pytest.raises(ValidationError):
        CarritoItem.objects.create(carrito=carrito, producto=producto, cantidad=2, precio=5990)

    # Intentamos crear un CarritoItem sin especificar la cantidad
    with pytest.raises(ValidationError):
        CarritoItem.objects.create(carrito=carrito, producto=producto, precio=5990)

    # Intentamos crear un CarritoItem sin especificar el precio
    with pytest.raises(ValidationError):
        CarritoItem.objects.create(carrito=carrito, producto=producto, cantidad=2)

# =======================================================================
# TEST CREAR PEDIDO
# =======================================================================

@pytest.mark.django_db
def test_crear_pedido():
    usuario = User.objects.create_user(username='testuser', password='12345')
    carrito = Carrito.objects.create(usuario=usuario)
    pedido = Pedido.objects.create(usuario=usuario, carrito=carrito, direccion_envio="123 Main St", metodo_pago="Tarjeta")

    assert pedido.usuario == usuario
    assert pedido.carrito == carrito
    assert pedido.estado == 'pendiente'
    assert pedido.direccion_envio == "123 Main St"
    assert pedido.metodo_pago == "Tarjeta"
    assert str(pedido) == f"Pedido {pedido.id} - {usuario} - pendiente"

# Crear pedidos sin campos
def test_crear_pedido_sin_campos():
    usuario = User.objects.create_user(username='testuser', password='12345')
    carrito = Carrito.objects.create(usuario=usuario)
    
    # Intentamos crear un Pedido sin especificar la dirección de envío y método de pago
    with pytest.raises(ValidationError):
        Pedido.objects.create(usuario=usuario, carrito=carrito)

# =======================================================================
# TEST CREAR DETALLE PEDIDO 
# =======================================================================
@pytest.mark.django_db
def test_crear_detalle_pedido():
    usuario = User.objects.create_user(username='testuser', password='12345')
    categoria_producto = CategoriaProducto.objects.create(categoria="Gasfiteria")
    tipo_producto = TipoProducto.objects.create(tipo="Lubricante")
    producto = Producto.objects.create(nombre="Cierra electrica", precio=5990, stock=55, descripcion="Cierra de buena calidad")
    producto.categoria.set([categoria_producto])
    producto.tipo.set([tipo_producto])
    carrito = Carrito.objects.create(usuario=usuario)
    pedido = Pedido.objects.create(usuario=usuario, carrito=carrito, direccion_envio="123 Main St", metodo_pago="Tarjeta")
    detalle_pedido = DetallePedido.objects.create(pedido=pedido, producto=producto, cantidad=2, precio=5990, subtotal=2*5990)
    
    assert detalle_pedido.pedido == pedido
    assert detalle_pedido.producto == producto
    assert detalle_pedido.cantidad == 2
    assert detalle_pedido.precio == 5990
    assert detalle_pedido.subtotal == 2 * 5990
    assert str(detalle_pedido) == f"Pedido {pedido.id} - Producto {producto.nombre} - Cantidad {detalle_pedido.cantidad}"

# TEST CREAR DETALLE PEDIDO SIN CAMPOS
@pytest.mark.django_db
def test_crear_detalle_pedido_sin_campos():
    usuario = User.objects.create_user(username='testuser', password='12345')
    categoria_producto = CategoriaProducto.objects.create(categoria="Gasfiteria")
    tipo_producto = TipoProducto.objects.create(tipo="Lubricante")
    producto = Producto.objects.create(nombre="Cierra electrica", precio=5990, stock=55, descripcion="Cierra de buena calidad")
    producto.categoria.set([categoria_producto])
    producto.tipo.set([tipo_producto])
    carrito = Carrito.objects.create(usuario=usuario)
    pedido = Pedido.objects.create(usuario=usuario, carrito=carrito, direccion_envio="123 Main St", metodo_pago="Tarjeta")
    
    # Intentamos crear un DetallePedido sin especificar el precio y subtotal
    with pytest.raises(ValidationError):
        DetallePedido.objects.create(pedido=pedido, producto=producto, cantidad=2)

# =======================================================================
# TEST CREAR BOLETA
# =======================================================================
@pytest.mark.django_db
def test_crear_boleta():
    usuario = User.objects.create_user(username='testuser', password='12345')
    boleta = Boleta.objects.create(usuario=usuario, total=11980)

    assert boleta.usuario == usuario
    assert boleta.total == 11980
    assert str(boleta.usuario) == 'testuser'

# TEST CREAR BOLETA SIN CAMPOS
@pytest.mark.django_db
def test_crear_boleta_sin_campos():
    usuario = User.objects.create_user(username='testuser', password='12345')
    
    # Intentamos crear una Boleta sin especificar el total
    with pytest.raises(ValidationError):
        Boleta.objects.create(usuario=usuario)


# =======================================================================
# TEST CREAR DETALLE BOLETA
# =======================================================================
@pytest.mark.django_db
def test_crear_detalle_boleta():
    usuario = User.objects.create_user(username='testuser', password='12345')
    categoria_producto = CategoriaProducto.objects.create(categoria="Gasfiteria")
    tipo_producto = TipoProducto.objects.create(tipo="Lubricante")
    producto = Producto.objects.create(nombre="Cierra electrica", precio=5990, stock=55, descripcion="Cierra de buena calidad")
    producto.categoria.set([categoria_producto])
    producto.tipo.set([tipo_producto])
    boleta = Boleta.objects.create(usuario=usuario, total=11980)
    detalle_boleta = DetalleBoleta.objects.create(boleta=boleta, producto=producto, cantidad=2, subtotal=11980)

    assert detalle_boleta.boleta == boleta
    assert detalle_boleta.producto == producto
    assert detalle_boleta.cantidad == 2
    assert detalle_boleta.subtotal == 11980

# TEST CREAR DETALLE BOLETA SIN CAMPOS
@pytest.mark.django_db
def test_crear_detalle_boleta_sin_campos():
    usuario = User.objects.create_user(username='testuser', password='12345')
    categoria_producto = CategoriaProducto.objects.create(categoria="Gasfiteria")
    tipo_producto = TipoProducto.objects.create(tipo="Lubricante")
    producto = Producto.objects.create(nombre="Cierra electrica", precio=5990, stock=55, descripcion="Cierra de buena calidad")
    producto.categoria.set([categoria_producto])
    producto.tipo.set([tipo_producto])
    boleta = Boleta.objects.create(usuario=usuario, total=11980)
    
    # Intentamos crear un DetalleBoleta sin especificar la cantidad
    with pytest.raises(ValidationError):
        DetalleBoleta.objects.create(boleta=boleta, producto=producto, subtotal=11980)

# =======================================================================
# TEST CREAR FORMULARIO DE CONTACTO
# =======================================================================
@pytest.mark.django_db
def test_form_contacto():

    data = {
        "nombre" : "Carlos Pardo Belmar",
        "email" : "car.pardo@duocuc.cl",
        "mensaje" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce posuere risus odio, ac dapibus nibh dignissim non. Nulla facilisi. Donec sit amet elit gravida, finibus tortor et, facilisis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer ullamcorper lacus eget eleifend iaculis. Nullam ullamcorper mollis ornare. Vivamus urna nunc, finibus in urna vitae, sodales viverra sapien. Duis id vehicula nunc. Ut porta scelerisque sodales. Maecenas vitae risus libero. Etiam sit amet lectus lorem. Donec eget tellus massa. Curabitur aliquam libero magna, et egestas ante bibendum tristique. Donec ac risus et odio tristique pellentesque. Proin erat ex, rutrum ut cursus id, suscipit ac leo. In ut pharetra quam."
    }
    form = ContactoForm(data = data)
    assert form.is_valid()

# TEST CREAR FORMULARIO DE CONTACTO SIN EMAIL
@pytest.mark.django_db
def test_form_contacto_con_error():
    data = {
        "nombre": "Carlos Pardo Belmar",
        "mensaje": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce posuere risus odio, ac dapibus nibh dignissim non. Nulla facilisi. Donec sit amet elit gravida, finibus tortor et, facilisis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer ullamcorper lacus eget eleifend iaculis. Nullam ullamcorper mollis ornare. Vivamus urna nunc, finibus in urna vitae, sodales viverra sapien. Duis id vehicula nunc. Ut porta scelerisque sodales. Maecenas vitae risus libero. Etiam sit amet lectus lorem. Donec eget tellus massa. Curabitur aliquam libero magna, et egestas ante bibendum tristique. Donec ac risus et odio tristique pellentesque. Proin erat ex, rutrum ut cursus id, suscipit ac leo. In ut pharetra quam."
    }
    form = ContactoForm(data=data)

    # Verificar que al intentar validar el formulario se lance un ValidationError
    with pytest.raises(ValidationError):
        form.is_valid()