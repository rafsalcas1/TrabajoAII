from django.urls import path
from UsersApp import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

]