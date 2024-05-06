from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate,login as login_aut
from django.contrib.auth.models import User
from .models import *
from .forms import *
import requests
from rest_framework import viewsets
from .serializers import *


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class TipoProductoViewset(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class ProductoOfertaViewset(viewsets.ModelViewSet):
    queryset = ProductoOferta.objects.all()
    serializer_class = ProductoOfertaSerializer

def index(request):
    response = requests.get('http://127.0.0.1:8000/api/Producto%20en%20oferta/')
    listado_productos = response.json()




    context = {
        'listado': listado_productos  
    }

    return render(request, 'index.html', context)

def login(request):
    if request.POST:
        username =request.POST.get("username")
        password =request.POST.get("password")
        user= authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login_aut(request,user)
            return redirect(to="index")
    return render(request,'../templates/registration/login.html')

def register(request):
    if request.POST:
        username = request.POST.get("username")
        email = request.POST.get("email")
        number = request.POST.get("number")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat-password")

        user = User()

        user.set_password(password)
        user.username = username
        user.email = email
        user.number = number

        try:
            if password == repeat_password:
                user.save()
                return redirect(to="LOGIN")
            print()
        except:
            print()
    return render(request, '../templates/registration/register.html')



def productos(request):
    response = requests.get('http://127.0.0.1:8000/api/productos/')

    data = response.json()
    listado_productos = data


    context = {
        'listado': listado_productos,
            }

        
    return render(request, 'productos.html', context)
