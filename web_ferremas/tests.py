from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.models import User

class TestCategoria(TestCase):
    def test_crear(self):
        categoria = CategoriaProducto.objects.create(categoria='Gasfiteria')
        self.assertEqual(categoria.categoria, 'Gasfiteria')

    def test_sin_nombre(self):
        categoria = CategoriaProducto(categoria='')
        with self.assertRaises(ValidationError) as context:
            categoria.full_clean()
        self.assertIn('El campo categoria no puede estar vacío.', str(context.exception))

    def test_nombre_corto(self):
        categoria = CategoriaProducto(categoria='Ga')
        with self.assertRaises(ValidationError) as context:
            categoria.full_clean()
        self.assertIn('El nombre de categoria debe tener al menos 3 caracteres.', str(context.exception))

    def test_nombre_largo(self):
        categoria = CategoriaProducto(categoria='Gasfiteria del primer mundo!')
        with self.assertRaises(ValidationError) as context:
            categoria.full_clean()
        self.assertIn('El nombre de categoria no puede tener más de 25 caracteres.', str(context.exception))

class TestTipo(TestCase):
    def test_crear(self):
        tipo = TipoProducto.objects.create(tipo='Herramientas de corte')
        self.assertEqual(tipo.tipo, 'Herramientas de corte')

    def test_sin_nombre(self):
        tipo = TipoProducto(tipo='')
        with self.assertRaises(ValidationError) as context:
            tipo.full_clean()
        self.assertIn('El campo tipo no puede estar vacío.', str(context.exception))

    def test_nombre_corto(self):
        tipo = TipoProducto(tipo='He')
        with self.assertRaises(ValidationError) as context:
            tipo.full_clean()
        self.assertIn('El nombre de tipo debe tener al menos 3 caracteres.', str(context.exception))

    def test_nombre_largo(self):
        tipo = TipoProducto(tipo='Herramientas de cortes de metales especiales')
        with self.assertRaises(ValidationError) as context:
            tipo.full_clean()
        self.assertIn('El nombre de tipo no puede tener más de 25 caracteres.', str(context.exception))

class TestProducto(TestCase):
    def test_crear(self):
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')

        producto = Producto.objects.create(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )

        producto.categoria.add(categoria)
        producto.tipo.add(tipo)

        self.assertEqual(producto.nombre, 'Martillo')
        self.assertEqual(producto.precio, 9990)
        self.assertEqual(producto.stock, 50)
        self.assertEqual(producto.descripcion, 'Breve Descripcion del producto')
        self.assertFalse(producto.en_oferta)
        self.assertIn(categoria, producto.categoria.all())
        self.assertIn(tipo, producto.tipo.all())

    def test_sin_nombre(self):
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')

        producto = Producto(
            nombre='',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.save()
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)

        with self.assertRaises(ValidationError) as context:
            producto.full_clean()
        self.assertIn('El campo "nombre" no puede estar vacío.', str(context.exception))

    def test_precio_invalido(self):
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')

        producto = Producto(
            nombre='Martillo',
            precio=0,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.save()
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)

        with self.assertRaises(ValidationError) as context:
            producto.full_clean()
        self.assertIn('El precio debe ser mayor que cero.', str(context.exception))

    def test_sin_categoria(self):
        tipo = TipoProducto.objects.create(tipo='Manual')

        producto = Producto(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.save()
        producto.tipo.add(tipo)

        with self.assertRaises(ValidationError) as context:
            producto.full_clean()
        self.assertIn('El campo "categoria" no puede estar vacio.', str(context.exception))

    def test_sin_tipo(self):
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')

        producto = Producto(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.save()
        producto.categoria.add(categoria)

        with self.assertRaises(ValidationError) as context:
            producto.full_clean()
        self.assertIn('El campo "tipo" no puede estar vacio.', str(context.exception))

class TestOfertaProducto(TestCase):
    def test_crear(self):
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')

        producto = Producto.objects.create(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=True
        )
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)

        oferta = ProductoOferta.objects.create(
            producto=producto,
            precio_oferta=7990
        )

        self.assertEqual(oferta.producto.nombre, 'Martillo')
        self.assertEqual(oferta.precio_oferta, 7990)

    def test_precio_oferta_invalido(self):
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')

        producto = Producto.objects.create(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=True
        )
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)

        oferta = ProductoOferta(
            producto=producto,
            precio_oferta=-2
        )

        with self.assertRaises(ValidationError) as context:
            oferta.full_clean()

        self.assertIn('El precio oferta no puede ser negativo.', str(context.exception))


class TestCarrito(TestCase):
    def test_crear_carrito(self):
        usuario = User.objects.create_user(username='testuser', password='12345')
        carrito = Carrito.objects.create(usuario=usuario)
        self.assertEqual(carrito.usuario.username, 'testuser')

    def test_sin_usuario(self):
        carrito = Carrito()
        with self.assertRaises(ValidationError) as context:
            carrito.full_clean()
        self.assertIn('Debe especificar un usuario para crear un carrito.', str(context.exception))

class TestCarritoItem(TestCase):
    def test_crear_carrito_item(self):
        usuario = User.objects.create_user(username='testuser', password='12345')
        carrito = Carrito.objects.create(usuario=usuario)
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')
        producto = Producto.objects.create(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)
        carrito_item = CarritoItem.objects.create(carrito=carrito, producto=producto, cantidad=1, precio=9990)
        self.assertEqual(carrito_item.carrito.usuario.username, 'testuser')

    def test_sin_carrito(self):
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')
        producto = Producto.objects.create(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)
        carrito_item = CarritoItem(producto=producto, cantidad=1, precio=9990)
        with self.assertRaises(ValidationError) as context:
            carrito_item.full_clean()
        self.assertIn('Debe especificar un carrito para crear un carrito item.', str(context.exception))

class TestPedido(TestCase):
    def test_crear_pedido(self):
        usuario = User.objects.create_user(username='testuser', password='12345')
        carrito = Carrito.objects.create(usuario=usuario)
        pedido = Pedido.objects.create(usuario=usuario, carrito=carrito)
        self.assertEqual(pedido.usuario.username, 'testuser')

    def test_sin_usuario(self):
        carrito = Carrito.objects.create(usuario=User.objects.create_user(username='testuser', password='12345'))
        pedido = Pedido(carrito=carrito)
        with self.assertRaises(ValidationError) as context:
            pedido.full_clean()
        self.assertIn('Este campo no puede ser nulo.', str(context.exception))

class TestDetallePedido(TestCase):
    def test_crear_detalle_pedido(self):
        usuario = User.objects.create_user(username='testuser', password='12345')
        carrito = Carrito.objects.create(usuario=usuario)
        pedido = Pedido.objects.create(usuario=usuario, carrito=carrito)
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')
        producto = Producto.objects.create(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)
        detalle_pedido = DetallePedido.objects.create(pedido=pedido, producto=producto, cantidad=1, precio=9990, subtotal=9990)
        self.assertEqual(detalle_pedido.pedido.usuario.username, 'testuser')

class TestBoleta(TestCase):
    def test_crear_boleta(self):
        usuario = User.objects.create_user(username='testuser', password='12345')
        boleta = Boleta.objects.create(usuario=usuario, total=9990)
        self.assertEqual(boleta.usuario.username, 'testuser')

class TestDetalleBoleta(TestCase):
    def test_crear_detalle_boleta(self):
        usuario = User.objects.create_user(username='testuser', password='12345')
        boleta = Boleta.objects.create(usuario=usuario, total=9990)
        categoria = CategoriaProducto.objects.create(categoria='Herramientas')
        tipo = TipoProducto.objects.create(tipo='Manual')
        producto = Producto.objects.create(
            nombre='Martillo',
            precio=9990,
            stock=50,
            descripcion='Breve Descripcion del producto',
            en_oferta=False
        )
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)
        detalle_boleta = DetalleBoleta.objects.create(boleta=boleta, producto=producto, cantidad=1, subtotal=9990)
        self.assertEqual(detalle_boleta.boleta.usuario.username, 'testuser')

class TestContacto(TestCase):
    def test_crear_contacto_valido(self):
        contacto = Contacto.objects.create(
            nombre='Juan Perez',
            email='juan.perez@example.com',
            mensaje='Hola, necesito información.'
        )
        self.assertEqual(contacto.nombre, 'Juan Perez')
        self.assertEqual(contacto.email, 'juan.perez@example.com')
        self.assertEqual(contacto.mensaje, 'Hola, necesito información.')

    def test_nombre_vacio(self):
        contacto = Contacto(nombre='', email='juan.perez@example.com', mensaje='Hola, necesito información.')
        with self.assertRaises(ValidationError) as context:
            contacto.full_clean()
        self.assertIn('El campo "nombre" no puede estar vacio.', str(context.exception))

    def test_nombre_demasiado_corto(self):
        contacto = Contacto(nombre='Jo', email='juan.perez@example.com', mensaje='Hola, necesito información.')
        with self.assertRaises(ValidationError) as context:
            contacto.full_clean()
        self.assertIn('El campo "nombre" debe tener al menos 3 caracteres', str(context.exception))

    def test_nombre_demasiado_largo(self):
        contacto = Contacto(nombre='J' * 31, email='juan.perez@example.com', mensaje='Hola, necesito información.')
        with self.assertRaises(ValidationError) as context:
            contacto.full_clean()
        self.assertIn('El campo "nombre" no puede tener mas de 30 caracteres', str(context.exception))

    def test_email_vacio(self):
        contacto = Contacto(nombre='Juan Perez', email='', mensaje='Hola, necesito información.')
        with self.assertRaises(ValidationError) as context:
            contacto.full_clean()
        self.assertIn('El campo "email" no puede esta vacio', str(context.exception))

    def test_email_demasiado_largo(self):
        contacto = Contacto(nombre='Juan Perez', email='a' * 101 + '@example.com', mensaje='Hola, necesito información.')
        with self.assertRaises(ValidationError) as context:
            contacto.full_clean()
        self.assertIn('El campo "email" no puede tener mas de 100 caracteres', str(context.exception))

    def test_mensaje_vacio(self):
        contacto = Contacto(nombre='Juan Perez', email='juan.perez@example.com', mensaje='')
        with self.assertRaises(ValidationError) as context:
            contacto.full_clean()
        self.assertIn('El campo "mensaje" no puede estar vacio.', str(context.exception))