# Generated by Django 4.2.7 on 2023-11-30 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_perro_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='numero_documento',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_documento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tipodocumento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sucursal'),
        ),
    ]