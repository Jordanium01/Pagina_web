# Generated by Django 4.0.4 on 2022-07-11 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_userextrainfo_username_id_userextrainfo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextrainfo',
            name='direccion',
            field=models.CharField(default='', max_length=300, verbose_name='Direccion: '),
        ),
    ]