from django.db import models

class Eventos(models.Model):
	"""docstring for Eventos"""
	nombre = models.CharField(max_length = 255)

	def __str__(self):
		return self.nombre
		
