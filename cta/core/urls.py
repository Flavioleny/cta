from django.conf.urls import url

from cta.core.views import home, cadastro_usuario, sucesso_usuario,\
user_login, user_logout, consulta_agendamento, consulta_atendimento,\
consulta_fornecedor, consulta_representante, consulta_objetivovisita, email_contato

urlpatterns = [
    url(r'^$', user_login, name='userlogin'),
    url(r'^home/$', home, name='home'),
    url(r'^logout/$', user_logout, name='userlogout'),    
    url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
    url(r'^consulta-agendamento/$', consulta_agendamento, name='consultaagendamento'),
    url(r'^consulta-atendimento/$', consulta_atendimento, name='consultaatendimento'),
    url(r'^consulta-fornecedor/$', consulta_fornecedor, name='consultafornecedor'),
    url(r'^consulta-representante/$', consulta_representante, name='consultarepresentante'),
    url(r'^consulta-objetivovisita/$', consulta_objetivovisita, name='consultaobjetivovisita'),
    url(r'^email-contato/$', email_contato, name='contato'),
]