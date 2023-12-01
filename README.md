# El Sabueso Feliz

[Descripción](#Descripción)

[Instalacion](#instalación)

[Diagrama Clases](#ClassDiagram)


# Descripción 

Este proyecto esta diseñado para la facilitación de las base datos de la veterinaria El Sabueso Feliz.
Este proyecto le permite al dueño de la veterinaria el registro de sus empleados,  sucursales nuevas.
A su vez tanto los empleados como dueño/administrador pueden registrar perros nuevos que vayan a la veterinaria, así también como agregar y ver las consultas.


## Registrar un empleado 
(Solo el administrador puede hacerlo)
1- Seleccionar la opción "Registrar empleado "
2- Completar el formulario con los datos necesarios

## Agregar un perro
(Lo pueden realizar los empleados y el administrador)
1- Seleccionar la opción "Registrar Perro"
2- Completar el formulario con los datos necesarios
## Agregar nueva sucursal
(Solo el administrador puede hacerlo)
1- Seleccionar la opción "Sucursales"
2- Ingresar la dirección de la sucursal
3- Cargar sucursal


## Detalles de Consulta
- Realizar consulta con los datos necesarios
- Enviar consulta
- Visualizar consultas anteriores
## Detalles Razas
- Visualizar las razas
- Visualizar cuidados especiales
- Visualizar diferentes características de la raza



# Instalación

### Requisitos Previos

Pipenv requerido:

```bash
    pip install pipenv
```
<hr>


### Creación del  Entorno Virtual

Es importante trabajar en entornos virtuales para evitar problemas que se relacionen con las dependencias de bibliotecas y paquetes. Utilizamos los siguientes  comandos para establecer y activar nuestro entorno virtual:

```bash
    pipenv install //Creacion
    pipenv shell //Ejecucion
```

### Instalación de los paquetes

Una vez dentro del entorno virtual, instalamos todos los paquetes necesarios para desarrollar y ejecutar el proyecto. Esto se logra con el siguiente comando:

```bash
    pipenv install -r requirements.txt
```


### Iniciar servidor local

Para arrancar el servidor local y visualizar el proyecto, utiliza el siguiente comando:

```bash 
python manage.py runserver
```

Este comando iniciará el servidor y permitirá que accedas al proyecto de manera local. Asegúrate de tener tu entorno virtual activado para asegurar de que funcione bien.

# ClassDiagram

![[mermaid-diagram-2023-12-01-011944.svg]]