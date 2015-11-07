from django.db import models

# Create your models here.

class Fornecedor(models.Model):
	#choices_pessoa=(('F','Fisica'),('J','Juridica'))
	#choices_atividade=(('C','Comercial'),('D','Distribuidor'),('I','Industria'))
    id = models.AutoField(primary_key=True)
    atividade = models.CharField(u'Atividade',max_length=1,choices=(('C','Comercial'),('D','Distribuidor'),('I','Industria')))
    prazopagamento = models.CharField(max_length=20)
    tipopessoa = models.CharField(u'Pessoa',max_length=1,choices=(('F','Fisica'),('J','Juridica')))
    representante = models.CharField(max_length=30)
    razaosocial = models.CharField(max_length=50)
    cgccpf = models.CharField(u'Cgccpf', max_length=18, help_text='99.999.999/9999-99')
    endereco = models.CharField(max_length=60)
    complemento = models.CharField(max_length=30)
    cep = models.CharField(u'Cep', max_length=10, help_text='99.999-999')
    bairro = models.CharField(max_length=30)
    cidade =  models.CharField(max_length=30, default='Teresina')
    estado =  models.CharField(max_length=2, default='PI')
    fone1 = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
    fone2 = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
    email = models.CharField(max_length=100)
    datacadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.nome

    class Meta:
        verbose_name='Fornecedor'
        verbose_name_plural='Fornecedor'        