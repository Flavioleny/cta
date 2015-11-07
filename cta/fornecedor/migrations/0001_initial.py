# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('atividade', models.CharField(verbose_name='Atividade', max_length=1, choices=[('C', 'Comercial'), ('D', 'Distribuidor'), ('I', 'Industria')])),
                ('prazopagamento', models.CharField(max_length=20)),
                ('tipopessoa', models.CharField(verbose_name='Pessoa', max_length=1, choices=[('F', 'Fisica'), ('J', 'Juridica')])),
                ('representante', models.CharField(max_length=30)),
                ('razaosocial', models.CharField(max_length=50)),
                ('cgccpf', models.CharField(help_text='99.999.999/9999-99', max_length=18, verbose_name='Cgccpf')),
                ('endereco', models.CharField(max_length=60)),
                ('complemento', models.CharField(max_length=30)),
                ('cep', models.CharField(help_text='99.999-999', max_length=10, verbose_name='Cep')),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(default='Teresina', max_length=30)),
                ('estado', models.CharField(default='PI', max_length=2)),
                ('fone1', models.CharField(help_text='(99)99999-9999', max_length=14, verbose_name='Celular')),
                ('fone2', models.CharField(help_text='(99)99999-9999', max_length=14, verbose_name='Celular')),
                ('email', models.CharField(max_length=100)),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
