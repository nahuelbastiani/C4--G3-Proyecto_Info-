from django.shortcuts import render
from eventos.models import Evento

def inicio(request):
	template_name = 'inicio.html'

	eventos = Evento.objects.all()

	ctx = {
		'eventos': eventos,
	}
	return render (request, template_name, ctx)

def registro(request):
    template_name = 'registro.html'
    
    ctx={}
    
    return render(request, template_name, ctx)

def perfil(request):
    template_name = 'perfil.html'
    
    ctx={}
    
    return render(request, template_name, ctx)

