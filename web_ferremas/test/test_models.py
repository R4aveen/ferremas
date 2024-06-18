from django.test import TestCase
from web_ferremas.models import CategoriaProducto, TipoProducto, Producto

### TESTING PARA LOS MODELS

class TipoProductoTestCase(TestCase):
    def test_crear_tipoproducto(self):
        tipo = TipoProducto.objects.create(tipo='metalica')
        self.assertEqual(tipo.tipo, 'metalica')

    def test_str_tipoproducto(self):
        tipo = TipoProducto.objects.create(tipo='electrico')
        self.assertEqual(str(tipo), 'electrico')

class test_crear_producto(TestCase):
    def test_crear_producto(self):
        tipo = TipoProducto.objects.create(tipo='metalica')
        categoria = CategoriaProducto.objects.create(categoria='tuberia')
        producto = Producto.objects.create(nombre='tuberia de 1/2', precio=100, stock=10, descripcion='tuberia de 1/2 pulgada', imagen='tuberia.jpg', en_oferta=False)
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)
        self.assertEqual(producto.nombre, 'tuberia de 1/2')
        self.assertEqual(producto.precio, 100)
        self.assertEqual(producto.stock, 10)
        self.assertEqual(producto.descripcion, 'tuberia de 1/2 pulgada')
        self.assertEqual(producto.imagen, 'tuberia.jpg')
        self.assertEqual(producto.en_oferta, False)
        self.assertEqual(producto.categoria.all()[0].categoria, 'tuberia')
        self.assertEqual(producto.tipo.all()[0].tipo, 'metalica')

    def test_str_producto(self):
        tipo = TipoProducto.objects.create(tipo='metalica')
        categoria = CategoriaProducto.objects.create(categoria='tuberia')
        producto = Producto.objects.create(nombre='tuberia de 1/2', precio=100, stock=10, descripcion='tuberia de 1/2 pulgada', imagen='tuberia.jpg', en_oferta=False)
        producto.categoria.add(categoria)
        producto.tipo.add(tipo)
        self.assertEqual(str(producto), 'tuberia de 1/2')