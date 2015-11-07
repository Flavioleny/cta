"""cta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from cta.core import urls as core_urls
from cta.agendamento import urls as agendamento_urls
from cta.atendimento import urls as atendimento_urls
from cta.fornecedor import urls as fornecedor_urls
from cta.objetivovisita import urls as objetivovisita_urls
from cta.representante import urls as representante_urls

from django.conf import settings

urlpatterns = [
	url(r'', include(core_urls, namespace='core')),
	url(r'', include(agendamento_urls, namespace='agendamento')),
	url(r'', include(atendimento_urls, namespace='atendimento')),
	url(r'', include(fornecedor_urls, namespace='fornecedor')),
	url(r'', include(objetivovisita_urls, namespace='objetivovisita')),
    url(r'', include(representante_urls, namespace='representante')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),    
]
