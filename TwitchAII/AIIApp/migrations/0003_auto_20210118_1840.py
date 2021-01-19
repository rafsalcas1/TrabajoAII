# Generated by Django 3.1.4 on 2021-01-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIIApp', '0002_auto_20210118_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
            ],
        ),
        migrations.RenameModel(
            old_name='Streamer',
            new_name='Actor',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
