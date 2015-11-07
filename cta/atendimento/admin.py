from django.contrib import admin

from cta.atendimento.models import Atendimento

# Register your models here.

class AtendimentoProfileAdmin(admin.ModelAdmin):
	list_display = ("id", "atendente","dataatendimento","horainicial","horafinal","representante",\
	"objetivoatendimento","status","conteudoatendimento","observacao")

admin.site.register(Atendimento, AtendimentoProfileAdmin)	