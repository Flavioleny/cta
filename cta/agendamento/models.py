from django.db import models

# Create your models here.

class Agendamento(models.Model):
	choices_status=(('A','Agendado'),('F','Finalizado'))
	id = models.AutoField(primary_key=True)
	atendente = models.CharField(max_length=20)
	dataagendamento = models.DateTimeField(auto_now_add=True)
	dataatendimento = models.DateTimeField()
	#horaatendimento = models.CharField(max_length=8)
	representante = models.CharField(max_length=50)
	objetivoatendimento = models.CharField(max_length=20)
	status = models.CharField(u'Status',max_length=1,choices=choices_status) #(Agendado, Em Atendimento e Finalizado);
	observacao = models.CharField(max_length=100)

	def __str__(self):
	    return self.atendente

	class Meta:
		verbose_name='Agendamento'
		verbose_name_plural='Agendamento'