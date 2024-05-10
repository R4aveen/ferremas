from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('Tipos de producto', TipoProductoViewset)
router.register('Producto en oferta', ProductoOfertaViewset)
router.register('Carrito de compras', CarritoViewset)

urlpatterns = [
    path('', index, name="index"),
    path('login/', LoginView.as_view(), name='LOGIN'), # type: ignore
    path('register/', register, name='REGISTER'),
    path('productos/', productos, name='productos'),
    path('api/', include(router.urls)),
    path('carrito/', carrito_de_compras, name='carrito_de_compras'),

    path('agregar-al-carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('api/carrito/eliminar/<int:carrito_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('api/carrito/decrementar/<int:carrito_id>/', decrementar_cantidad_carrito, name='decrementar_cantidad_carrito'),


    ]


#### quedamos en revisar lo de la api rest full