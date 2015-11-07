from django.conf.urls import url

from cta.objetivovisita.views import cadastro_objetivo_visita, apagar_objetivovisita, editar_objetivovisita


urlpatterns = [
    url(r'^cadastro-objetivovisita/$', cadastro_objetivo_visita, name='objetivovisita'),
    url(r'^deletar-objetivovisita/(?P<id>\d+)/$', apagar_objetivovisita, name='apagarobjetivovisita'),
    url(r'^editar-objetivovisita/(?P<id>\d+)/$', editar_objetivovisita, name='editarobjetivovisita'),
]