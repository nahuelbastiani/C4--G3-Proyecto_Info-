from django.contrib.auth import authenticate, login
from django.shortcuts import render
from eventos.models import Evento
from django.urls import reverse

def inicio(request):
	template_name = 'inicio.html'

	eventos = Evento.objects.all()
	

	ctx = {
		'eventos': eventos,
	}
	return render (request, template_name, ctx)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return reverse('/inicio')
        else:
            # Return a 'disabled account' error message
            ...
    else: 
        # Return an 'invalid login' error message.
        ...
    return render(request, "login.html", {})