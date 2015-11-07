from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from cta.representante.forms import RepresentanteForm
from cta.representante.models import Representante

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'core:userlogin')
def cadastro_representante(request):
	newcadastro = 'S'
	if request.method == 'POST':
		representante_form = RepresentanteForm(request.POST, request.FILES)
		if representante_form.is_valid():
			representante_form.save()
			representante_form = RepresentanteForm()
			return render(request, 'cadastro_representante.html', {'representante_form': representante_form, 'newcadastro': newcadastro})
			#mensg = "Representante Cadastrado com Sucesso..."
			#render(request,'cadastro_representante.html', {'mensg': mensg})
	else:
		representante_form = RepresentanteForm()

	return render(request, 'cadastro_representante.html', {'representante_form': representante_form, 'newcadastro': newcadastro})

def apagar_representante(request, id):
	representantes = Representante.objects.get(id=id).delete()
	return redirect(reverse('core:consultarepresentante'))	

def editar_representante(request,id):
	representantes = Representante.objects.get(id=id)
	newcadastro = 'N'
	if request.method == 'POST':
		representante_form = RepresentanteForm(request.POST, instance=representantes)
		if representante_form.is_valid:
			representante_form.save()
			return redirect(reverse('core:consultarepresentante'))
		else:
			print(representante_form.errors)
	else:
		representante_form = RepresentanteForm(instance=representantes)
	
	return render(request, 'cadastro_representante.html',{'representante_form':representante_form, 'newcadastro': newcadastro})
