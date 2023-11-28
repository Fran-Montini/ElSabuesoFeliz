from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from app.models import *
from django.contrib.auth import *
from django.db.utils import *
from django.http import HttpResponse, HttpRequest
from django.contrib import  messages
from django.urls import reverse
def home(request):
    return redirect("/login")

def base(request):
    return render(request,'./Veterinaria_list.html')
    
def login_empleado(request):
    return render(request,"./LoginEmpleado.html")

def login_perro(request):
    if request.method == 'GET':
        razas = Raza.objects.all()
        return render(request, './LoginPerros.html', {"razas" : razas})
    
    elif request.method == 'POST':
        perro = request.POST["Nombre"]
        raza = request.POST["Raza"]
        peso = request.POST["pesoActual"]
        sexo = request.POST["sexo"]
        fechaNacimiento = request.POST["fechaNacimiento"]
        altura = request.POST["alturaActual"]
        consulta = request.POST["consulta"]
        razaful = Raza.objects.get(denominacion = raza)
        p = Perro.objects.create(nombre=perro,raza=razaful,pesoActual=peso,sexo=sexo,fechaNacimiento=fechaNacimiento,alturaActual=altura,consulta=consulta)    
        return redirect("/veterinaria")
def razaperro(request):
    return render(request, 'razaperro_template.html')

def loginview(request: HttpRequest):
    
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            
            request.session["user"] = username
            
            return redirect("/veterinaria")  
        else:
            messages.success(request,("Las credenciales no coinciden"))
            return redirect('/login')
    
