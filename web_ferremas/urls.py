from django.urls import path, include
from .views import *

urlpatterns = [
    path('base/', base, name='BASE'),
    path('', index, name='INDEX'),
    path('login/', login, name='LOGIN'),
    path('cerrar_sesion/', cerrar_sesion, name='CERRAR_SESION'),
    path('registro/', registro, name='REGISTRO'),
    path('productos/', productos, name='PRODUCTOS'),
    path('crud_productos/', crud_productos, name='CRUD_PRODUCTOS'),

    # CARRITO
    path('carrito/', carrito, name='CARRITO'),

    # METODOS PRINCIPALES
    path('agregar/<int:id_producto>/', agregar_al_carrito, name='AGREGAR_AL_CARRITO'),
    path('eliminar/<int:id_item>/', eliminar_del_carrito, name='ELIMINAR_DEL_CARRITO'),
    path('vaciar/', vaciar_carrito, name='VACIAR_CARRITO'),

    # AUMENTAR Y DISMINUR CANTIDAD
    path('aumentar/<int:id_item>/', aumentar_cantidad, name='AUMENTAR_CANTIDAD'),
    path('disminuir/<int:id_item>/', disminuir_cantidad, name='DISMINUIR_CANTIDAD'),

    # MERCADO PAGO
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('failure/', failure, name='failure'),
    path('pending/', pending, name='pending'),
]