# Generated by Django 4.0.4 on 2022-05-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0005_juego_distribuidora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribuidorajuego',
            name='fechaCreacionDistribudora',
        ),
        migrations.AddField(
            model_name='distribuidorajuego',
            name='fundacionDistribuidora',
            field=models.CharField(default=0, max_length=30, verbose_name='Fundacion'),
            preserve_default=False,
        ),
    ]
