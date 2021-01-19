from django.urls import path
from AIIApp import views

urlpatterns = [
    path('peliculas', views.lista_peliculas),
    path('actores', views.actores, name="Actores"),
    path('about', views.about, name="About"),
    path('carga',views.carga),

]