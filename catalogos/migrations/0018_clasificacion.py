# Generated by Django 4.0.4 on 2022-05-30 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0017_alter_juego_annosalida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('idClasificacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('pais', models.CharField(max_length=50, verbose_name='Pais')),
                ('promedio', models.IntegerField(verbose_name='Promedio jugadores:')),
                ('fecha', models.DateField(verbose_name='Updates:')),
                ('recaudado', models.IntegerField(verbose_name='Dinero recaudado:')),
                ('juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.juego')),
            ],
        ),
    ]