from django.contrib import admin

from cta.objetivovisita.models import Objetivovisita

# Register your models here.

class ObjetivovisitaProfileAdmin(admin.ModelAdmin):
	list_display = ("id", "titulo")

admin.site.register(Objetivovisita, ObjetivovisitaProfileAdmin)	