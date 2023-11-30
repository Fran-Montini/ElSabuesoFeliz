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
    
    if request.method == 'GET':
        tipo_documento = Tipodocumento.objects.all()
        sucursal = Sucursal.objects.all()
        return render(request, './LoginEmpleado.html', {"tipo_documentos" : tipo_documento, 'sucursales' : sucursal})
    
    if request.method == 'POST':
        username = request.POST['username-empleado']
        pass_empleado = request.POST['pass-empleado']
        nombre = request.POST['nombre-empleado']
        apellido = request.POST['apellido-empleado']
        correo = request.POST['email-empleado']
        nro_documento = request.POST['nro-documento-empleado']
        sexo = request.POST['sexo']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        fecha_ingreso = request.POST['fecha_ingreso']

    if 'sucursal' in request.POST:
        sucursal = request.POST['sucursal']

    if 'tipodocumento' in request.POST:
        tipo_documento_id = request.POST['tipodocumento']
    else:
        tipo_documento_id = None  # O cualquier valor predeterminado que sea apropiado en tu caso


        
        if Usuario.objects.filter(username=username).exists():
            error_message = "El nombre de usuario ya está en uso."
        
        elif Usuario.objects.filter(email=correo).exists():
            error_message = "El correo electrónico ya está en uso."
             
        else:
        
                hashed_password = make_password(pass_empleado)
                user = Usuario.objects.create_user(
                    username=username,
                    password=hashed_password,  
                    nombre=nombre,  
                    apellido=apellido,
                    email=correo,
                    is_active = 'True',
                    tipodocumento = Tipodocumento.objects.get(id = tipo_documento_id), 
                    numero_documento=nro_documento,                    sexo = sexo,
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
        #ciudades = Ciudad.objects.all(),'ciudades' : ciudades}
        return render(request, 'sucursal.html', {'sucursales': sucursales})

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
        raise ("Raza inexistente")

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
    
