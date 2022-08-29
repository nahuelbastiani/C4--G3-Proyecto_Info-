from email import message
from gc import get_objects
from pyexpat.errors import messages
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from eventos.models import Evento, Asistencia

from django.views.generic import ListView, CreateView

from django.http import HttpResponseRedirect

from usuarios.models import Usuario
from .forms import Asistir

def listarEventos(request):
	template_name = 'eventos/listar.html'
	form = Asistir(initial={'id_id_Usuario':'mercadillo@mail.com', 'id_Evento':'s'})
	print('formmmmmmmm', form)
	eventos = Evento.objects.all().values('id_evento','titulo', 'categoria')
	
	print(eventos) 

	if request.method =="POST":
		#asistencia = Asistencia(id_Evento=)
		form = Asistir(request.POST)
		# form.id_Usuario = get_object_or_404(Usuario, pk=request.user.pk)
		# form.id_Evento = request.POST.get('event_id')
		# print('id eventoooooooo', request.POST.get('event_id'))
		# print('formmmmmmmmmm', form.id_Usuario)
		if form.is_valid():
			form.save()

	ctx = {
		'eventos': eventos,
		'form':form
	}
	print('contextoo', ctx)
	return render (request, template_name, ctx)



# def asistir(request):
# 	template_name = 'eventos/listar.html'
# 	if request.method == 'POST':
# 		asiste = Asistir(request.POST)
	
# 	return render(request, template_name, {'asiste': asiste})

# class Asistir(CreateView):
# 	template_name =  'eventos/listar.html'
# 	model = Asistencia

# def asistir_usuario(request):
# 	current_user = get_object_or_404(Usuario, pk=request.user.pk)
# 	print ('current user', current_user)
# 	if request.method == 'POST':
# 		form = Asistir(request.POST)
# 		print('-------->', request.POST.get('event_id'))
# 		#if form.is_valid():
# 		var = form.save(commit=False)
# 		print('esto tiene varrrr', var)
# 		var.user = current_user
# 		var.id_evento = request.POST.get('event_id')
# 		var.save()
# 		messages.success(request, 'Asistencia Confirmada')
# 		return redirect ('eventos/listar')
# 	else:
# 		return redirect ('listar')