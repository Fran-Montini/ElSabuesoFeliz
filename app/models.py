from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


''' para el registro, agregar campo de usuario y contraseña en el html
    hacer un post al momento de apretar el boton
    para crear usuario es Usuario.objects.create_user(username='', password='')
'''
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El campo de nombre de usuario es obligatorio")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(username, password, **extra_fields)

class Pais(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.nombre

        
class Sucursal(models.Model):
    direccion = models.CharField(max_length=255)
    

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def agregarConsulta(self, consulta):
        self.consultas.append(consulta)
    def __str__(self) -> str:
        return self.direccion
    

class Tipodocumento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombrePersona = models.CharField(max_length=255)
    tipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE, null=True)
    numDocPersona = models.IntegerField("Numero de Documento", null=True)
    descripcion = models.CharField(("Descripcion:"), max_length=180)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(('Email'), max_length=254)
    nombre = models.CharField(('Nombre'),max_length=255)
    apellido = models.CharField(('Apellido'),max_length=255)
    fechaNacimiento = models.DateField(('FechaNacimiento'),null=True)
    fechaIngreso = models.DateField(('FechaDeIngreso'),null=True)
    sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE ,null=True)
    empleado = models.BooleanField(('Empleado'),default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    tipo_documento = models.ForeignKey(Tipodocumento,on_delete=models.CASCADE ,null=True)
    numero_documento = models.CharField(max_length = 30)
    sexo = models.CharField(max_length=255)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "nombres", "apellido"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} - {self.nombre} {self.apellido}"



class AsignacionEmpleados(models.Model):
    fechaIngreso = models.DateField()
    fechaEgreso = models.DateField()
    descripcion = models.CharField(max_length=255)



    def verificarEstadoEmpleado(self):
        pass
 
class Perro(models.Model):
    numeroHistoriaClinica = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    raza = models.ForeignKey('Raza', on_delete=models.CASCADE)
    pesoActual = models.FloatField()
    alturaActual = models.FloatField()
    sexo = models.CharField(max_length=255)
    historialMascotas = models.ForeignKey('HistorialMascotas', on_delete=models.CASCADE ,null=True)
    consulta = models.TextField(null=True)  
    vacuna = models.CharField(("vacuna;"), max_length=100,null=True)
    sucursal = models.ForeignKey("Sucursal", on_delete=models.CASCADE)

    def generarNumHistoriaClinica(self):
        pass

    def verificarPersona(self):
        pass

    def identificarVacunacion(self):
        pass
    def __str__(self) -> str:
        return self.nombre
class HistorialMascotas(models.Model):
    estadoPerro = models.CharField(max_length=255)
    rolPersona = models.CharField(max_length=255)

    def verificarEstadoPerro(self):
        pass

    def verificarRolPersona(self):
        pass



class Raza(models.Model):
    denominacion = models.CharField(max_length=255)
    pesoMinimoMachos = models.FloatField()
    pesoMaximoMachos = models.FloatField()
    pesoMinimoHembras = models.FloatField()
    pesoMaximoHembras = models.FloatField()
    alturaMediaMachos = models.FloatField()
    alturaMediaHembras = models.FloatField()
    cuidadosEspeciales = models.CharField(("cuidadosEspeciales"), max_length=180)
    def __str__(self) -> str:
        return self.denominacion

class Consulta(models.Model):
    numeroOrden = models.IntegerField(primary_key=True, auto_created=True)
    fechaEntrada = models.DateField()
    sIntomas = models.CharField(max_length=255)
    diagnosticos = models.CharField(max_length=255)
    medicamento = models.CharField(max_length=255)
    fechaSalida = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE, related_name='consultas')

    def verificarPersona(self):
        pass

    def verificarRolEmpleadoConsulta(self):
        pass

    def identificarNumHistoriaClinica(self):
        pass

    def recetarMedicamentos(self):
        pass

    def verificarPerro(self):
        pass

class Vacunacion(models.Model):
    fechaProgramada = models.DateField()
    fechaReal = models.DateField()
    descripcion = models.CharField(max_length=255)

class Vacuna(models.Model):
    nombreVacuna = models.CharField(max_length=255)
    empleado = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    fechaUltimaCompra = models.DateField()
    cantidadExistente = models.IntegerField()
    cantidadMinima = models.IntegerField()

class EstadoEmpleado(models.Model):
    estudiante = models.CharField(max_length=255)
    recibido = models.CharField(max_length=255)
    trabaja = models.CharField(max_length=255)
    noTrabaja = models.CharField(max_length=255)

class RolEmpleado(models.Model):
    supervisor = models.CharField(max_length=255)
    supervisorSuplente = models.CharField(max_length=255)
