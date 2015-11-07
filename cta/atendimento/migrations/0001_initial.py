# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('atendente', models.CharField(max_length=20)),
                ('dataatendimento', models.DateTimeField(auto_now_add=True)),
                ('horainicial', models.DateTimeField(auto_now_add=True)),
                ('horafinal', models.DateTimeField(auto_now_add=True)),
                ('representante', models.CharField(max_length=50)),
                ('objetivoatendimento', models.CharField(max_length=20)),
                ('status', models.CharField(verbose_name='Status', max_length=1, choices=[('E', 'Em Atendimento'), ('F', 'Finalizado')])),
                ('conteudoatendimento', models.TextField(max_length=200)),
                ('observação', models.CharField(max_length=100)),
            ],
        ),
    ]
