# Generated by Django 4.2.7 on 2023-11-29 20:12

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionEmpleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField()),
                ('fechaEgreso', models.DateField()),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.CharField(max_length=255)),
                ('recibido', models.CharField(max_length=255)),
                ('trabaja', models.CharField(max_length=255)),
                ('noTrabaja', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoPerro', models.CharField(max_length=255)),
                ('rolPersona', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('laboratorio', models.CharField(max_length=255)),
                ('fechaUltimaCompra', models.DateField()),
                ('cantidadExistente', models.IntegerField()),
                ('cantidadMinima', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=255)),
                ('numDocPersona', models.IntegerField()),
                ('descripcion', models.CharField(max_length=180, verbose_name='Descripcion:')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=255)),
                ('pesoMinimoMachos', models.FloatField()),
                ('pesoMaximoMachos', models.FloatField()),
                ('pesoMinimoHembras', models.FloatField()),
                ('pesoMaximoHembras', models.FloatField()),
                ('alturaMediaMachos', models.FloatField()),
                ('alturaMediaHembras', models.FloatField()),
                ('cuidadosEspeciales', models.CharField(max_length=180, verbose_name='cuidadosEspeciales')),
            ],
        ),
        migrations.CreateModel(
            name='RolEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor', models.CharField(max_length=255)),
                ('supervisorSuplente', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreVacuna', models.CharField(max_length=255)),
                ('empleado', models.CharField(max_length=255)),
                ('laboratorio', models.CharField(max_length=255)),
                ('dosis', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacunacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaProgramada', models.DateField()),
                ('fechaReal', models.DateField()),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('numeroHistoriaClinica', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('fechaNacimiento', models.DateField()),
                ('pesoActual', models.FloatField()),
                ('alturaActual', models.FloatField()),
                ('sexo', models.CharField(max_length=255)),
                ('consulta', models.TextField(null=True)),
                ('vacuna', models.CharField(max_length=100, null=True, verbose_name='vacuna;')),
                ('historialMascotas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.historialmascotas')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.raza')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroOrden', models.IntegerField()),
                ('fechaEntrada', models.DateField()),
                ('sIntomas', models.CharField(max_length=255)),
                ('diagnosticos', models.CharField(max_length=255)),
                ('medicamento', models.CharField(max_length=255)),
                ('fechaSalida', models.DateField()),
                ('perro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='app.perro')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('nombres', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
                ('fechaNacimiento', models.DateField(null=True, verbose_name='FechaNacimiento')),
                ('fechaIngreso', models.DateField(null=True, verbose_name='FechaDeIngreso')),
                ('empleado', models.BooleanField(default=True, verbose_name='Empleado')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('sucursal', models.ForeignKey(null=True, on_delete=app.models.Sucursal, to='app.sucursal')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
