# Generated by Django 4.0.4 on 2022-06-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0021_rename_idclasificacionjuego_clasificacion_idclasificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Correo')),
                ('pnombre', models.CharField(max_length=100, verbose_name='PNombre')),
                ('snombre', models.CharField(max_length=100, verbose_name='SNombre')),
                ('apaterno', models.CharField(max_length=100, verbose_name='APaterno')),
                ('amaterno', models.CharField(max_length=100, verbose_name='AMaterno')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
                ('clave', models.CharField(max_length=16, verbose_name='clave')),
            ],
        ),
    ]
