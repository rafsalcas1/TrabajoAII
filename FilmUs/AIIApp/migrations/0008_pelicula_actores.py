# Generated by Django 3.1.4 on 2021-01-18 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIIApp', '0007_pelicula_generos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='actores',
            field=models.ManyToManyField(to='AIIApp.Actor'),
        ),
    ]