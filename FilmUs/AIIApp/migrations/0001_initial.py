# Generated by Django 3.1.4 on 2021-01-18 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Género')),
            ],
        ),
        migrations.CreateModel(
            name='Streamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('pais', models.TextField(verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('empresa', models.TextField(verbose_name='Empresa')),
                ('fechaLanzamiento', models.DateField(verbose_name='FechaLanzamiento')),
                ('generos', models.ManyToManyField(to='AIIApp.Genero')),
            ],
        ),
    ]
