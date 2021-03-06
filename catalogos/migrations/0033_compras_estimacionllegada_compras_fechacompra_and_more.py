# Generated by Django 4.0.4 on 2022-07-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0032_remove_compras_estimacionllegada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='estimacionllegada',
            field=models.DateTimeField(null=True, verbose_name='fecha de estimacion de llegada'),
        ),
        migrations.AddField(
            model_name='compras',
            name='fechaCompra',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='fecha de compra'),
        ),
        migrations.AddField(
            model_name='compras',
            name='fechallegada',
            field=models.DateTimeField(null=True, verbose_name='fecha de llegada'),
        ),
    ]
