
from django.shortcuts import  render, redirect
from .form import UsuarioRegistroForm
from django.contrib.auth import login
from django.contrib import messages
from usuarios.models import Usuario
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def register_request(request):
    if request.method == "POST":
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("inicio")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UsuarioRegistroForm()
    return render (request=request, template_name="usuarios/registro.html", context={"register_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Te has deslogueado correctamente.") 
    return redirect("inicio")

"""def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("inicio")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="usuarios/login.html", context={"login_form":form})"""

