#encoding:utf-8
from AIIApp.models import Genero, Pelicula, Actor
#from AIIApp.forms import BusquedaPorFechaForm, BusquedaPorGeneroForm
from bs4 import BeautifulSoup
import urllib.request
import lxml
from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from urllib.request import Request, urlopen
import re

# Create your views here.

def actores(request):

    return HttpResponse("Actores")

def about(request):

    return HttpResponse("About")

#función auxiliar que hace scraping en la web y carga los datos en la base datos
def populateDB():
    #variables para contar el número de registros que vamos a almacenar
    num_peliculas = 0
    num_generos = 0
    num_actores = 0
    
    #borramos todas las tablas de la BD
    Pelicula.objects.all().delete()
    Genero.objects.all().delete()
    Actor.objects.all().delete()
    
    #extraemos los datos de la web con BS
    f = urllib.request.urlopen("https://www.themoviedb.org/movie/top-rated?language=es-ES")
    s = BeautifulSoup(f, "lxml")
    lista_link_peliculas = s.find("div", class_="page_wrapper").find_all("div", class_="card style_1")
    for link_pelicula in lista_link_peliculas:
        f = urllib.request.urlopen("https://www.themoviedb.org"+link_pelicula.find("h2").a['href'])
        s = BeautifulSoup(f, "lxml")
        datos = s.find("section", class_="header poster")
        titulo = datos.find("h2").find("a").string.strip()
        result = re.sub(r'\([^)]*\)', '', datos.find("span",class_="release").string.strip()).strip()
        fecha_estreno = datetime.strptime(result,'%d/%m/%Y')
        duracion = datos.find("span",class_="runtime").string.strip()
        resumen = datos.find("div",class_="overview").find("p").string.strip()
        generos = datos.find("span",class_="genres").find_all("a")
        lista_generos_obj = []
        for genero in generos:
            genero = genero.string.strip()
            genero_obj, creado = Genero.objects.get_or_create(nombre=genero)
            lista_generos_obj.append(genero_obj)
            if creado:
                num_generos = num_generos + 1
        actores = s.find("div", class_="scroller_wrap should_fade is_fading").find_all("li", class_="card")
        lista_actores_obj = []
        for actor in actores:
            actor = actor.find("p").find("a").string.strip()
            print(actor)
            actor_obj, creado = Actor.objects.get_or_create(nombre=actor)
            lista_actores_obj.append(actor_obj)
            if creado:
                num_actores = num_actores + 1

        p = Pelicula.objects.create(titulo = titulo, fecha_estreno = fecha_estreno,
                                duracion = duracion,
                                resumen = resumen)
        
        #añadimos la lista de géneros
        for g in lista_generos_obj:
            p.generos.add(g)
        
        #añadimos la lista de actores
        for a in lista_actores_obj:
            p.actores.add(a)
        
        num_peliculas = num_peliculas + 1

    return ((num_peliculas, num_generos, num_actores))
           
#carga los datos desde la web en la BD
def carga(request):

    if request.method=='POST':
        if 'Aceptar' in request.POST:      
            num_peliculas = populateDB()
            mensaje="Se han almacenado: " + str(num_peliculas) +" peliculas"
            return render(request, 'cargaBD.html', {'mensaje':mensaje})
        else:
            return redirect("/")

    return render(request, 'confirmacion.html')

#muestra el número de películas que hay en la BD
def inicio(request):
    num_peliculas=Pelicula.objects.all().count()
    return render(request,'home.html', {'num_peliculas':num_peliculas})

#muestra un listado con los datos de las películas (título, título original, país, director, géneros y fecha de estreno)
def lista_peliculas(request):
    peliculas=Pelicula.objects.all()
    return render(request,'peliculas.html', {'peliculas':peliculas})
