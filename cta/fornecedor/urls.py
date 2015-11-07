from django.conf.urls import url

from cta.fornecedor.views import cadastro_fornecedor, apagar_fornecedor, editar_fornecedor


urlpatterns = [
    url(r'^cadastro-fornecedor/$', cadastro_fornecedor, name='fornecedor'),
    url(r'^deletar-fornecedor/(?P<id>\d+)/$', apagar_fornecedor, name='apagarfornecedor'),
    url(r'^editar-fornecedor/(?P<id>\d+)/$', editar_fornecedor, name='editarfornecedor'),
]