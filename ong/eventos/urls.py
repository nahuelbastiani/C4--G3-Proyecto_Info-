
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'eventos'

urlpatterns = [
    path('perfil/', views.perfil, name= 'perfil'),
    path('listar/', views.Listar.as_view(), name= 'listar'),
    #path('eliminarEvento/<pk>', views.eliminar, name = 'eliminarEvento')
]