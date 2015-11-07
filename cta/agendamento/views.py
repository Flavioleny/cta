from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from cta.agendamento.forms import AgendamentoForm
from cta.agendamento.models import Agendamento

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'core:userlogin')
def form_agendamento(request):
	newcadastro = 'S'
	if request.method == 'POST':
		agendamento_form = AgendamentoForm(request.POST, request.FILES)
		if agendamento_form.is_valid():
			agendamento_form.save()
			agendamento_form = AgendamentoForm()
			return render(request, 'form_agendamento.html', {'agendamento_form': agendamento_form, 'newcadastro': newcadastro})			
			#return redirect('/')
	else:
		agendamento_form = AgendamentoForm()

	return render(request, 'form_agendamento.html', {'agendamento_form': agendamento_form, 'newcadastro': newcadastro})

def apagar_agendamento(request, id):
	agendamentos = Agendamento.objects.get(id=id).delete()
	return redirect(reverse('core:consultaagendamento'))	

def editar_agendamento(request,id):
	agendamentos = Agendamento.objects.get(id=id)
	newcadastro = 'N'
	if request.method == 'POST':
		agendamento_form = AgendamentoForm(request.POST, instance=agendamentos)
		if agendamento_form.is_valid:
			agendamento_form.save()
			return redirect(reverse('core:consultaagendamento'))
		else:
			print(agendamento_form.errors)
	else:
		agendamento_form = AgendamentoForm(instance=agendamentos)
	
	return render(request, 'form_agendamento.html',{'agendamento_form':agendamento_form, 'newcadastro': newcadastro})
