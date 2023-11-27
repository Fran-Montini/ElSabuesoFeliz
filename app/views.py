from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from app.models import *
from django.contrib.auth import *
from django.db.utils import *
from django.http import HttpRequest
from django.contrib import  messages

def home(request):
    return render(request, "./login.html")

def base(request):
    return render(request,'./Veterinaria_list.html')
    
def login_empleado(request):
    return render(request,"./LoginEmpleado.html")

def login_perro(request):
    if request.method == 'GET':
        return render(request, './LoginPerros.html')
    
    else:
        perro = request.POST["Nombre"]
        raza =request.POST["Raza"]
        peso = request.POST["Peso"]
        sexo = request.POST["genero"]
        p = Perro.objects.create(nombre=perro,raza=raza,peso=peso,sexo=sexo)
        print (p)

def razaperro(request):
    return render(request, 'razaperro_template.html')

def loginview(request: HttpRequest):
    if request.method == "GET" and request.session.get("user"):
        return redirect('./login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            
            request.session["user"] = username
            
            return redirect('./Veterinaria_list.html')  
        else:
            messages.success(request,("Las credenciales no coinciden"))
            return redirect('./login.html')
    else:
        return render(request, './login.html', )

