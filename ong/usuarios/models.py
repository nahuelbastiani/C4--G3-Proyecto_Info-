from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class Usuario(AbstractUser):
    id_Usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    es_Admin = models.BooleanField(default=False)
    id_evento = models.ForeignKey('eventos.Evento', on_delete=models.CASCADE, null=True, blank=True)
    telefono= models.IntegerField(null=True, blank=True)