from django import forms

from cta.atendimento.models import Atendimento

class AtendimentoForm(forms.ModelForm):
	class Meta:
		model = Atendimento
		fields = ('atendente','representante', 'objetivoatendimento', 'status', 'conteudoatendimento','observacao')