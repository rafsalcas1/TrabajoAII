# Generated by Django 3.1.4 on 2021-01-18 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AIIApp', '0005_remove_pelicula_puntuacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='generos',
        ),
    ]
