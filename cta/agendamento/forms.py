from django import forms

from cta.agendamento.models import Agendamento

class AgendamentoForm(forms.ModelForm):
	class Meta:
		model = Agendamento
		fields = ('atendente','dataatendimento','representante','objetivoatendimento','status','observacao')