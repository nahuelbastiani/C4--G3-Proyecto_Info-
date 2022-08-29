from pyexpat import model
from django import forms 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from usuarios.models import Usuario


    

class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=Usuario
        fields=["username", "first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UsuarioRegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user