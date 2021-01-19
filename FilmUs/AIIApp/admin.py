from django.contrib import admin
from AIIApp.models import Pelicula, Actor, Genero

#registramos en el administrador de django los modelos 
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Actor)