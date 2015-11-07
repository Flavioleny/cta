from django import forms

from cta.fornecedor.models import Fornecedor

class FornecedorForm(forms.ModelForm):
	class Meta:
		model = Fornecedor
		fields = ('atividade', 'prazopagamento', 'tipopessoa', 'representante', \
			      'razaosocial','cgccpf','endereco','complemento','cep','bairro',\
			      'cidade','estado','fone1','fone2','email')