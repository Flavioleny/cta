from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

from .forms import UserForm, UserProfileForm
from cta.agendamento.models import Agendamento
from cta.atendimento.models import Atendimento

from cta.fornecedor.models import Fornecedor
from cta.representante.models import Representante
from cta.objetivovisita.models import Objetivovisita

# Create your views here.

from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'base.html')

def cadastro_usuario(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'foto' in request.FILES:
				profile.foto = request.FILES['foto']

			profile.save()
			return redirect('core:cadastrousuario') #core:usuariosucesso
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'core/cadastro_usuario.html',\
		{'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('core:home') #HttpResponse("Login feito com sucesso.")
			else:				
				mensg = "Sua conta esta desativada."
				return render(request,'core/form_login.html', {'mensg': mensg}) #HttpResponse("Sua conta esta desativada.")
		else:
			mensg = "Usuario ou senha invalido."
			return render(request,'core/form_login.html', {'mensg': mensg}) #HttpResponse("Usuario ou senha invalido.")
	return render(request, 'core/form_login.html')

def sucesso_usuario(request):
	return render(request, 'base.html') #core/sucesso_usuario.html

def user_logout(request):
    logout(request)
    return redirect('core:userlogin')

@login_required(login_url = 'core:userlogin')
def consulta_agendamento(request):
	agendamentos = Agendamento.objects.all() # [:15] --> numero de registro a ser visualizado, objects e igual a select * from tabela
	return render(request, 'core/consulta_agendamento.html', {'agendamentos': agendamentos})

@login_required(login_url = 'core:userlogin')
def consulta_atendimento(request):
	atendimentos = Atendimento.objects.all() # [:15] --> numero de registro a ser visualizado, objects e igual a select * from tabela
	return render(request, 'core/consulta_atendimento.html', {'atendimentos': atendimentos})

@login_required(login_url = 'core:userlogin')
def consulta_fornecedor(request):
	fornecedores = Fornecedor.objects.all() # [:15] --> numero de registro a ser visualizado, objects e igual a select * from tabela
	return render(request, 'core/consulta_fornecedor.html', {'fornecedores': fornecedores})

@login_required(login_url = 'core:userlogin')
def consulta_representante(request):
	representantes = Representante.objects.all() # [:15] --> numero de registro a ser visualizado, objects e igual a select * from tabela
	return render(request, 'core/consulta_representante.html', {'representantes': representantes})

@login_required(login_url = 'core:userlogin')
def consulta_objetivovisita(request):
	objetivovisitas = Objetivovisita.objects.all() # [:15] --> numero de registro a ser visualizado, objects e igual a select * from tabela
	return render(request, 'core/consulta_objetivovisita.html', {'objetivovisitas': objetivovisitas})

def email_contato(request):
	if request.method == 'POST':
		subject = request.POST.get('subject')
		message = request.POST.get('inputmessage')
		from_email = "flavioleny@gmail.com"
		for_email  = request.POST.get('inputemail')

		if subject and message and for_email:
			send_mail(subject, message, from_email, [for_email], fail_silently=True)

			mensg = "E-mail enviado com Sucesso..."
			return render(request,'core/contato.html', {'mensg': mensg})
		else:
			mensg = "Todos os campos são Obrigatorios."
			return render(request,'core/contato.html', {'mensg': mensg})
	else:
		return render(request, 'core/contato.html')