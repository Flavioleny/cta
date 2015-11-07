from django.conf.urls import url

from cta.atendimento.views import form_atendimento, apagar_atendimento, editar_atendimento


urlpatterns = [
    url(r'^formulario-atendimento/$', form_atendimento, name='atendimento'),
    url(r'^deletar-atendimento/(?P<id>\d+)/$', apagar_atendimento, name='apagaratendimento'),
    url(r'^editar-atendimento/(?P<id>\d+)/$', editar_atendimento, name='editaratendimento'),    
]