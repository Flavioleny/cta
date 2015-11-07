from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	telefone = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
	foto = models.ImageField(upload_to="media/profile", blank=True)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.first_name