# Generated by Django 4.0.4 on 2022-07-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtraInfo',
            fields=[
                ('username_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('is_suscribe', models.BooleanField(verbose_name='suscrito: ')),
            ],
        ),
    ]
