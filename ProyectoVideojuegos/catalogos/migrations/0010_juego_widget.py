# Generated by Django 4.0.4 on 2022-05-12 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0009_juego_distribuidora'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='widget',
            field=models.CharField(default=0, max_length=100, verbose_name='widget'),
            preserve_default=False,
        ),
    ]
