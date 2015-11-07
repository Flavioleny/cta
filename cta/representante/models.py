from django.db import models

# Create your models here.

class Representante(models.Model):
	id = models.AutoField(primary_key=True)
	nomerepresentante = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name='Representante'
		verbose_name_plural='Representante'		