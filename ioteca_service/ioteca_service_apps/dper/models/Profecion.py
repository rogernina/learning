from django.db import models

class Profecion(models.Model):
	nombreprofecion = models.CharField(max_length=70, null=False, blank=False)

	def __str__(self):
		
		return self.nombreprofecion




