from django.db import models

# Create your models here.

class Objetivovisita(models.Model):
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=20)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name='Objetivovisita'
		verbose_name_plural='Objetivovisita'