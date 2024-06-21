import pytest
from .models import *

@pytest.mark.django_db
def test_crear_categoria_producto():
    categoria_producto = CategoriaProducto.objects.create(
        categoria="Gasfiteria"
    )
    assert categoria_producto.categoria == "Gasfiteria"

@pytest.mark.django_db
def test_str_categoria_producto():
    categoria_producto = CategoriaProducto.objects.create(
        categoria="Gasfiteria"
    )
    assert str(categoria_producto) == "Gasfiteria"

@pytest.mark.django_db
def test_crear_tipo_producto():
    tipo_producto = TipoProducto.objects.create(
        tipo = "Lubricante"
    )
    assert tipo_producto.tipo == "Lubricante"

@pytest.mark.django_db
def test_crear_tipo_producto():
    tipo_producto = TipoProducto.objects.create(
        tipo = "Lubricante"
    )
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