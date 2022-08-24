from re import template
from django.shortcuts import render

from eventos.models import Eventos

def inicio(request):
	template_name = 'inicio.html'

	eventos = Eventos.objects.all()
	print(eventos)

	ctx = {
		'eventos': eventos,
	}
	return render (request, template_name, ctx)