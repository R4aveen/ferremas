from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('Tipos de producto', TipoProductoViewset)

urlpatterns = [
    path('', index, name="index"),
    path('login/', LoginView.as_view(), name='LOGIN'), # type: ignore
    path('register/', register, name='REGISTER'),
    path('productos/', productos, name='productos'),
    path('api/', include(router.urls)),

    ]