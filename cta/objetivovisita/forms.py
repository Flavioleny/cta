from django import forms

from cta.objetivovisita.models import Objetivovisita

class ObjetivovisitaForm(forms.ModelForm):
	class Meta:
		model = Objetivovisita
		fields = ('titulo',)