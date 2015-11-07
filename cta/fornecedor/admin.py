from django.contrib import admin

from .models import Fornecedor

# Register your models here.

class FornecedorProfileAdmin(admin.ModelAdmin):
	list_display = ("id", "atividade","prazopagamento","tipopessoa","representante","razaosocial",\
	"cgccpf","endereco","complemento","cep","bairro","cidade","estado","fone1","fone2","email","datacadastro")

admin.site.register(Fornecedor, FornecedorProfileAdmin)	
