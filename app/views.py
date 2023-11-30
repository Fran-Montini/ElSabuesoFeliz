from .models import *
from django.shortcuts import render, redirect
from app.models import *
from django.contrib.auth import *
from django.db.utils import *
from django.http import HttpResponse, HttpRequest
from django.contrib import  messages
from app.models import *
from django.contrib.auth.models import User

def home(request):
    return redirect("/login")

def base(request):
    return render(request,'./Veterinaria_list.html')

def login_empleado(request):
    tipo_documento_id = Tipodocumento.objects.all()
    sucursal = Sucursal.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        tipo_documento_id = request.POST['tipodocumento']
        documento = request.POST['documento']
        sexo = request.POST['sexo']
        sucursal = request.POST['sucursal']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        fecha_ingreso = request.POST['fecha_ingreso']


        
        if Usuario.objects.filter(username=username).exists():
            error_message = "El nombre de usuario ya está en uso."
        
        elif Usuario.objects.filter(email=email).exists():
            error_message = "El correo electrónico ya está en uso."

        elif Usuario.objects.filter(password=password).exists():
            error_message = "La contasenia ya esta en uso"
             
        else:
            user = Usuario.objects.create_user(
                username = username,
                password = password,
                first_name = first_name,
                last_name = last_name,
                email = email,
                is_active = 'True',
                tipodocumento = Tipodocumento.objects.get(id = tipo_documento_id), 
                documento = documento,
                sexo = sexo,
                sucursal = Sucursal.objects.get(id = sucursal),
                fecha_nacimiento = fecha_nacimiento,
                fecha_ingreso = fecha_ingreso
            )
            user.save()
            
            
        return redirect('/veterinaria')

    return render(request, './LoginEmpleado.html')

def sucursales(request):
    if request.method == 'GET':
        sucursales = Sucursal.objects.all()
        ciudades = Ciudad.objects.all()
        return render(request, 'sucursal.html', {'sucursales': sucursales, 'ciudades' : ciudades})

def consulta_menu(request):
    return render(request,"./consulta_menu.html")


def login_perro(request):
    if request.method == 'GET':
        razas = Raza.objects.all()
        sucursal = Sucursal.objects.all()
        return render(request, './LoginPerros.html', {"razas" : razas, 'sucursales' : sucursal})
    
    
    elif request.method == 'POST':
        perro = request.POST["Nombre"]
        raza = request.POST["Raza"]
        peso = request.POST["pesoActual"]
        sexo = request.POST["sexo"]
        fechaNacimiento = request.POST["fechaNacimiento"]
        altura = request.POST["alturaActual"]
        consulta = request.POST["consulta"]
        sucursal = request.POST ["Sucursal"]
        sucursalful = sucursal.objects.get(direccion = sucursal)
        razaful = Raza.objects.get(denominacion = raza)
        p = Perro.objects.create(nombre=perro,sucursal=sucursalful,raza=razaful,pesoActual=peso,sexo=sexo,fechaNacimiento=fechaNacimiento,alturaActual=altura,consulta=consulta)    
        return redirect("/veterinaria")
def razaperro(request):

    razas = Raza.objects.all()
    return render(request, 'Razas.html', {'razas': razas})

def detalles_raza(request, raza_id):
    
    try:
        raza = Raza.objects.get(pk=raza_id)
    except Raza.DoesNotExist:
        raise Http404("Raza inexistente")

    return render(request, 'detalles_raza.html', {'raza': raza})


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
    
