# Generated by Django 3.1.4 on 2021-01-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIIApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamer',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='streamer',
            name='rank',
        ),
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Genero'),
        ),
    ]