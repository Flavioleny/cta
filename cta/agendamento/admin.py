from django.contrib import admin

from cta.agendamento.models import Agendamento

# Register your models here.

class AgendamentoProfileAdmin(admin.ModelAdmin):
	list_display = ("id", "atendente","dataagendamento",\
	"representante","objetivoatendimento","status","observacao")

admin.site.register(Agendamento, AgendamentoProfileAdmin)	
