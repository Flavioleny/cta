from django.db import models

# Create your models here.

class Atendimento(models.Model):
	choices_status=(('E','Em Atendimento'),('F','Finalizado'))
	id = models.AutoField(primary_key=True)
	atendente = models.CharField(max_length=20)
	dataatendimento= models.DateTimeField(auto_now_add=True)
	horainicial = models.DateTimeField(auto_now_add=True)
	horafinal = models.DateTimeField(auto_now_add=True)
	representante = models.CharField(max_length=50)
	objetivoatendimento = models.CharField(max_length=20)
	status = models.CharField(u'Status',max_length=1,choices=choices_status) #(Em Atendimento e Finalizado);
	conteudoatendimento = models.TextField(max_length=200)
	observacao = models.CharField(max_length=100)

	def __str__(self):
		return self.atendente

	class Meta:
		verbose_name='Atendimento'
		verbose_name_plural='Atendimento'