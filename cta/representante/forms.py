from django import forms

from .models import Representante

class RepresentanteForm(forms.ModelForm):
	class Meta:
		model = Representante
		fields = ('id','nomerepresentante')