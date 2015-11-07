from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from cta.atendimento.forms import AtendimentoForm
from cta.atendimento.models import Atendimento

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'core:userlogin')
def form_atendimento(request):
	newcadastro = 'S'
	if request.method == 'POST':
		atendimento_form = AtendimentoForm(request.POST, request.FILES)
		if atendimento_form.is_valid():
			atendimento_form.save()
			atendimento_form = AtendimentoForm()
			return render(request, 'form_atendimento.html', {'atendimento_form': atendimento_form, 'newcadastro': newcadastro})			
			#return redirect('/')
	else:
		atendimento_form = AtendimentoForm()

	return render(request, 'form_atendimento.html', {'atendimento_form': atendimento_form, 'newcadastro': newcadastro})

def apagar_atendimento(request, id):
	atendimentos = Atendimento.objects.get(id=id).delete()
	return redirect(reverse('core:consultaatendimento'))	

def editar_atendimento(request,id):
	atendimentos = Atendimento.objects.get(id=id)
	newcadastro = 'N'
	if request.method == 'POST':
		atendimento_form = AtendimentoForm(request.POST, instance=atendimentos)
		if atendimento_form.is_valid:
			atendimento_form.save()
			return redirect(reverse('core:consultaatendimento'))
		else:
			print(atendimento_form.errors)
	else:
		atendimento_form = AtendimentoForm(instance=atendimentos)
	
	return render(request, 'form_atendimento.html',{'atendimento_form':atendimento_form, 'newcadastro': newcadastro})
