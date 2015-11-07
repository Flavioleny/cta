from django.conf.urls import url

from cta.agendamento.views import form_agendamento, apagar_agendamento, editar_agendamento


urlpatterns = [
    url(r'^formulario-agendamento/$', form_agendamento, name='agendamento'),
    url(r'^deletar-agendamento/(?P<id>\d+)/$', apagar_agendamento, name='apagaragendamento'),
    url(r'^editar-agendamento/(?P<id>\d+)/$', editar_agendamento, name='editaragendamento'),    
]