from django.conf.urls import url

from cta.representante.views import cadastro_representante, apagar_representante, editar_representante


urlpatterns = [
    url(r'^cadastro-representante/$', cadastro_representante, name='representante'),
    url(r'^deletar-representante/(?P<id>\d+)/$', apagar_representante, name='apagarrepresentante'),
    url(r'^editar-representante/(?P<id>\d+)/$', editar_representante, name='editarrepresentante'),
]