from django import forms
from django.forms import ModelForm

from eventos.models import Asistencia

class Asistir(ModelForm):
    #asistencia = forms.BooleanField()
    class Meta:
        model = Asistencia
        #widgets = {'id_Usuario': forms.HiddenInput(), 'id_Evento': forms.HiddenInput() }
        fields = '__all__'