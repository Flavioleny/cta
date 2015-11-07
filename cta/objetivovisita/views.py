from django.shortcuts import render, redirect
from django.http import HttpResponse

from cta.objetivovisita.forms import ObjetivovisitaForm
from cta.objetivovisita.models import Objetivovisita

from django.core.urlresolvers import reverse

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'core:userlogin')
def cadastro_objetivo_visita(request):
	newcadastro = 'S'
	if request.method == 'POST':
		objetivovisita_form = ObjetivovisitaForm(request.POST, request.FILES)
		if objetivovisita_form.is_valid():
			objetivovisita_form.save()
			objetivovisita_form = ObjetivovisitaForm()
			return render(request, 'cadastro_objetivo_visita.html', {'objetivovisita_form': objetivovisita_form, 'newcadastro': newcadastro}) 			
			#return redirect('/')
	else:
		objetivovisita_form = ObjetivovisitaForm()

	return render(request, 'cadastro_objetivo_visita.html', {'objetivovisita_form': objetivovisita_form, 'newcadastro': newcadastro})

def apagar_objetivovisita(request, id):
	objetivovisitas = Objetivovisita.objects.get(id=id).delete()
	return redirect(reverse('core:consultaobjetivovisita'))

def editar_objetivovisita(request,id):
	objetivovisitas = Objetivovisita.objects.get(id=id)
	newcadastro = 'N'
	if request.method == 'POST':
		objetivovisita_form = ObjetivovisitaForm(request.POST, instance=objetivovisitas)
		if objetivovisita_form.is_valid:
			objetivovisita_form.save()
			return redirect(reverse('core:consultaobjetivovisita'))
		else:
			print(objetivovisita_form.errors)
	else:
		objetivovisita_form = ObjetivovisitaForm(instance=objetivovisitas)
	
	return render(request, 'cadastro_objetivo_visita.html',{'objetivovisita_form':objetivovisita_form, 'newcadastro': newcadastro})