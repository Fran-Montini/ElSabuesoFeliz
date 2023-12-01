from .models import *
from django.shortcuts import render, redirect
from app.models import *
from django.contrib.auth import *
from django.db.utils import *
from django.http import HttpResponse, HttpRequest
from django.contrib import  messages
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return redirect("/login")

def base(request):
    logged_user = getLoggedUser(request)
    return render(request,'./Veterinaria_list.html',{"logged_user" : logged_user})

def login_empleado(request):
    logged_user = getLoggedUser(request)
    if request.method == 'GET':
        tipo_documento = Tipodocumento.objects.all()
        sucursales = Sucursal.objects.all()
        print(sucursales)
        return render(request, './LoginEmpleado.html', {"tipo_documentos" : tipo_documento, 'sucursales' : sucursales,"logged_user" : logged_user})
    
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
        print(correo)
        

  

    if 'Sucursal' in request.POST:
        sucursal = request.POST['Sucursal']
    else:
        sucursal = None

    if 'tipo_documento' in request.POST:
        tipo_documento = request.POST['tipo_documento']
    else:
        tipo_documento = None  # O cualquier valor predeterminado que sea apropiado en tu caso


    
    if Usuario.objects.filter(username=username).exists():
        error_message = "El nombre de usuario ya está en uso."
    
    elif Usuario.objects.filter(email=correo).exists():
        error_message = "El correo electrónico ya está en uso."
            
    hashed_password = make_password(pass_empleado)
    user = Usuario.objects.create(
        username = username,
        password = hashed_password,  
        nombre = nombre,  
        apellido = apellido,
        # email = correo,
        is_active = 'True',
        tipo_documento = Tipodocumento.objects.get(id = tipo_documento), 
        numero_documento=nro_documento,                    
        sexo = sexo,
        sucursal = Sucursal.objects.get(direccion=sucursal),
        fechaNacimiento = fecha_nacimiento,
        fechaIngreso = fecha_ingreso
    )
    user.save()
                 
                
            
    return redirect('/veterinaria')

#     return render(request, './LoginEmpleado.html')
# def login_empleado(request):
    
#     if request.method == 'GET':
#         tipo_documento = Tipodocumento.objects.all()
#         sucursal = Sucursal.objects.all()
#         return render(request, './LoginEmpleado.html', {"tipo_documentos": tipo_documento, 'sucursales': sucursal})
    
#     if request.method == 'POST':
#         username = request.POST.get('username-empleado', '')
#         pass_empleado = request.POST.get('pass-empleado', '')
#         nombre = request.POST.get('nombre-empleado', '')
#         apellido = request.POST.get('apellido-empleado', '')
#         correo = request.POST.get('email-empleado', '')
#         nro_documento = request.POST.get('nro-documento-empleado', '')
#         sexo = request.POST.get('sexo', '')
#         fecha_nacimiento = request.POST.get('fecha_nacimiento', '')
#         fecha_ingreso = request.POST.get('fecha_ingreso', '')

#         sucursal_id = request.POST.get('sucursal', '')
#         tipo_documento_id = request.POST.get('tipodocumento', '')

#         # Verifica si los IDs son cadenas vacías y establece valores predeterminados si es necesario
#         sucursal_id = sucursal_id if sucursal_id else None
#         tipo_documento_id = tipo_documento_id if tipo_documento_id else None

#         if Usuario.objects.filter(username=username).exists():
#             error_message = "El nombre de usuario ya está en uso."
#         elif Usuario.objects.filter(email=correo).exists():
#             error_message = "El correo electrónico ya está en uso."
#         else:
#             hashed_password = make_password(pass_empleado)
#             user = Usuario.objects.create_user(
#                 username=username,
#                 password=hashed_password,
#             )

#             # Ahora establece los campos adicionales
#             user.nombre = nombre
#             user.apellido = apellido
#             user.email = correo
#             user.is_active = True
#             user.tipodocumento_id = tipo_documento_id
#             user.numero_documento = nro_documento
#             user.sexo = sexo
#             user.sucursal_id = sucursal_id
#             user.fecha_nacimiento = fecha_nacimiento
#             user.fecha_ingreso = fecha_ingreso

#             user.save()
            
#             return redirect('/veterinaria')

#     return render(request, './LoginEmpleado.html')
def sucursales(request):
    logged_user = getLoggedUser(request)
    if request.method == 'GET':
        # sucursales = Sucursal.objects.all() 'sucursales': sucursales,
        return render(request, 'sucursal.html', {"logged_user" : logged_user})

    elif request.method == 'POST':
        sucursal = request.POST["direccion"]
        # sucursales = Sucursal.objects.get(direccion = sucursales)
        s = Sucursal.objects.create(direccion = sucursal)
        s.save()
        return redirect('/veterinaria')

def consulta_menu(request):
    logged_user = getLoggedUser(request)
    return render(request,"./consulta_menu.html",{"logged_user" : logged_user})


def login_perro(request):
    logged_user = getLoggedUser(request)
    if request.method == 'GET':
        razas = Raza.objects.all()
        sucursal = Sucursal.objects.all()
        return render(request, './LoginPerros.html', {"razas" : razas, 'sucursales' : sucursal,"logged_user" : logged_user})
    
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
        sucursalful = sucursal.objects.get(direccion = sucursal)
        p = Perro.objects.create(nombre=perro,sucursal=sucursalful,raza=razaful,pesoActual=peso,sexo=sexo,fechaNacimiento=fechaNacimiento,alturaActual=altura,consulta=consulta)    
        return redirect("/veterinaria")
def razaperro(request):
    logged_user = getLoggedUser(request)
    razas = Raza.objects.all()
    return render(request, 'Razas.html', {'razas': razas,"logged_user" : logged_user})

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
    
def getLoggedUser(request: HttpRequest):
    return request.session.get("user")


def agregar_consulta(request):
    logged_user = getLoggedUser(request)
    if request.method == 'GET':
        perros = Perro.objects.all()
        return render(request, './agregar_consulta.html', {"logged_user" : logged_user, 'perros' : perros})
    
    elif request.method == 'POST':
        fecha_entrada = request.POST['fecha_entrada']
        fecha_salida = request.POST['fecha_salida']
        sintomas = request.POST['sintomas']
        diagnosticos = request.POST['diagnosticos']
        medicamento = request.POST['medicamento']
        perro = Raza.objects.get(nombre = perro)
        c = Consulta.objects.create(fecha_entrada=fecha_entrada,fecha_salida=fecha_salida,sintomas=sintomas,diagnosticos=diagnosticos,medicamento=medicamento)  
        return redirect("/veterinaria") 

