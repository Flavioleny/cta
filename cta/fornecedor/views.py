from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.urlresolvers import reverse

from cta.fornecedor.forms import FornecedorForm
from cta.fornecedor.models import Fornecedor


# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url = 'core:userlogin')
def cadastro_fornecedor(request):
	newcadastro = 'S'
	if request.method == 'POST':
		fornecedor_form = FornecedorForm(request.POST, request.FILES)
		if fornecedor_form.is_valid():
			fornecedor_form.save()
			fornecedor_form = FornecedorForm()
			return render(request, 'cadastro_fornecedor.html', {'fornecedor_form': fornecedor_form, 'newcadastro': newcadastro})
			#return redirect('/')
	else:
		fornecedor_form = FornecedorForm()

	return render(request, 'cadastro_fornecedor.html', {'fornecedor_form': fornecedor_form, 'newcadastro': newcadastro})

def apagar_fornecedor(request, id):
	fornecedores = Fornecedor.objects.get(id=id).delete()
	return redirect(reverse('core:consultafornecedor'))

def editar_fornecedor(request,id):
	fornecedores = Fornecedor.objects.get(id=id)
	newcadastro = 'N'
	if request.method == 'POST':
		fornecedor_form = FornecedorForm(request.POST, instance=fornecedores)
		if fornecedor_form.is_valid:
			fornecedor_form.save()
			return redirect(reverse('core:consultafornecedor'))
		else:
			print(fornecedor_form.errors)
	else:
		fornecedor_form = FornecedorForm(instance=fornecedores)
	
	return render(request, 'cadastro_fornecedor.html',{'fornecedor_form':fornecedor_form, 'newcadastro': newcadastro})