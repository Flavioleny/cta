from django.contrib import admin

from .models import Representante

# Register your models here.

class RepresentanteProfileAdmin(admin.ModelAdmin):
	list_display = ("id", "nomerepresentante")

admin.site.register(Representante, RepresentanteProfileAdmin)