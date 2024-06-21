import pytest
from .models import *

@pytest.mark.django_db
def test_crear_categoria_producto():
    categoria_producto = CategoriaProducto.objects.create(
        categoria="Gasfiteria"
    )
    assert categoria_producto.categoria == "Gasfiteria"
    assert str(categoria_producto) == "Gasfiteria"

@pytest.mark.django_db
def test_crear_tipo_producto():
    tipo_producto = TipoProducto.objects.create(
        tipo = "Lubricante"
    )
    assert tipo_producto.tipo == "Lubricante"
    assert str(tipo_producto) == "Lubricante"

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
    
@pytest.mark.django_db
def test_crear_carrito():
    usuario = User.objects.create_user(username='testuser', password='12345')
    carrito = Carrito.objects.create(usuario=usuario)
    
    assert carrito.usuario == usuario
    assert carrito.pedido_aprobado == False
    assert str(carrito) == f"{usuario} - {carrito.creado_en}"

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

@pytest.mark.django_db
def test_crear_boleta():
    usuario = User.objects.create_user(username='testuser', password='12345')
    boleta = Boleta.objects.create(usuario=usuario, total=11980)

    assert boleta.usuario == usuario
    assert boleta.total == 11980
    assert str(boleta.usuario) == 'testuser'

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