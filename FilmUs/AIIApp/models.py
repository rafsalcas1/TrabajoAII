#encoding:utf-8
from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Genero')

    def __str__(self):
        return self.nombre
        
    
class Actor(models.Model):
    nombre = models.TextField(verbose_name='Nombre')

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.TextField(verbose_name='Titulo', null=True)
    fecha_estreno = models.DateField(verbose_name='Fecha estreno', null=True)
    duracion = models.TextField(verbose_name='Duración', null=True)
    resumen = models.TextField(verbose_name='Resumen', null=True)
    generos = models.ManyToManyField(Genero)
    actores = models.ManyToManyField(Actor)
    
    def __str__(self):
        return self.titulo