from django.contrib import admin
from .views import *
from django.urls import path 
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginview, name='loginview'),
    path('veterinaria/', base, name = 'Veterinarialist'),
    path('razas/', razaperro, name='Raza'),   
    path('registerperros/', login_perro, name='registrarperrro'),
    path('logEmpl/', login_empleado, name="loginEmpleado"),
    path('consulta/', consulta_menu, name="consultas"),
    path('sucursales/', sucursal, name="sucursales"),
]
