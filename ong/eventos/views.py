from django.shortcuts import render
#from evento.models import *

def listarEventos(request):
	template_name = 'eventos/listar.html'

	eventos = 'hola mundo'#Evento.objects.all()
	print(eventos) 

	ctx = {
		'eventos': eventos,
	}
	return render (request, template_name, ctx)