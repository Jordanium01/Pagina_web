# Generated by Django 4.0.1 on 2022-07-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0026_alter_clasificacion_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='precio',
            field=models.IntegerField(default=0, verbose_name='precio:'),
            preserve_default=False,
        ),
    ]
