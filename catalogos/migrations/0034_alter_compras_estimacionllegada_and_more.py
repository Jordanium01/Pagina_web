# Generated by Django 4.0.4 on 2022-07-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0033_compras_estimacionllegada_compras_fechacompra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='estimacionllegada',
            field=models.DateTimeField(null=True, verbose_name='fecha de estimacion de llegada:'),
        ),
        migrations.AlterField(
            model_name='compras',
            name='fechaCompra',
            field=models.DateTimeField(null=True, verbose_name='fecha de compra:'),
        ),
        migrations.AlterField(
            model_name='compras',
            name='fechallegada',
            field=models.DateTimeField(null=True, verbose_name='fecha de llegada:'),
        ),
    ]
