from django.shortcuts import render
from eventos.models import Evento
from django.views.generic.edit import CreateView
from usuarios.models import Usuario
from django.contrib.auth import login, authenticate, logout



def inicio(request):
	template_name = 'inicio.html'

	eventos = Evento.objects.all()
	ctx = {
		'eventos': eventos,
	}
	return render (request, template_name, ctx)

def iniciar_sesion(request):
	template_name = 'authenticate/login.html'

	ctx = {}

	return render (request, template_name, ctx)










		
