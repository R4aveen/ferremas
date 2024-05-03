from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', index, name="index"),
    path('login/', LoginView.as_view(), name='LOGIN'), # type: ignore
    path('register/', register, name='REGISTER'),
    path('productos/', productos, name='productos'),
    ]