from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate,login as login_aut
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    return render(request, 'productos.html')