from django import forms
from django.contrib.auth.models import User

from cta.core.models import UserProfile

class UserForm(forms.ModelForm):
	#first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user', 'data_cadastro')