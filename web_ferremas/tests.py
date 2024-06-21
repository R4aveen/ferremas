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