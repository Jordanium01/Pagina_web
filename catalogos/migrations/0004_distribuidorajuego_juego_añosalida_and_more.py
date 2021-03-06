# Generated by Django 4.0.4 on 2022-05-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0003_remove_juego_foto_juego_caratula_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistribuidoraJuego',
            fields=[
                ('idDistribuidora', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreDistribuidora', models.CharField(max_length=30, verbose_name='Nombre')),
                ('logoDistribuidora', models.ImageField(upload_to='files/logoDistribuidora', verbose_name='Logo')),
                ('fechaCreacionDistribudora', models.CharField(max_length=30, verbose_name='fechaCreacion')),
            ],
        ),
        migrations.AddField(
            model_name='juego',
            name='añoSalida',
            field=models.CharField(default=0, max_length=20, verbose_name='AñoSalida'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='juego',
            name='caratula',
            field=models.ImageField(upload_to='files/caratulas', verbose_name='Caratula'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.CharField(max_length=500, verbose_name='Descripcion'),
        ),
    ]
