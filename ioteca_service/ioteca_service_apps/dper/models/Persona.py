from django.db import models
from .Profecion import Profecion

class Persona(models.Model):
	nombre = models.CharField(max_length = 15, null=False, blank=False)     
	appaterno = models.CharField(max_length = 15, null = False, blank= False )
	apmaterno = models.CharField(max_length = 15, null = False, blank = False)
	edad = models.IntegerField()
	imagen = models.ImageField(upload_to = 'media')
	profecion = models.ForeignKey (Profecion) 

	def __str__ (self):
		return "%s %s %s" % (self.nombre, self.appaterno, self.apmaterno)

