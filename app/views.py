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
        return redirect('veterinaria/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            
            request.session["user"] = username
            
            print("dsdsd")
            return redirect('veterinaria/')  
        else:
            messages.success(request,("Las credenciales no coinciden"))
            return redirect('./login.html')
    else:
        return render(request, './login.html', )

#class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return render(request, self.template_name, ("./Veterinaria_list.html").format(user))
        else:
            return render(request, self.template_name, {'error_message': 'Credenciales inválidas'})
