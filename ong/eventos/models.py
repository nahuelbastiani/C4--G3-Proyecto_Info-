from django.db import models

# Create your models here.

import uuid


class Evento(models.Model):
    id_evento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    fecha = models.DateField()
    entrada = models.IntegerField()
    modalidad = models.BooleanField()
    lugar = models.CharField(max_length=255)
    detalles = models.CharField(max_length=255)
    id_usuario= models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)

    def __str__(self):
        fila = f'Evento: {self.titulo}'
        return fila
    
class Asistencia(models.Model):
    id_Asistencia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_Usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    id_Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        fila = f'Evento: {self.id_evento}'
        return fila



