# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('atendente', models.CharField(max_length=20)),
                ('dataagendamento', models.DateField(auto_now_add=True)),
                ('dataatendimento', models.DateField(auto_now_add=True)),
                ('representante', models.CharField(max_length=50)),
                ('objetivoatendimento', models.CharField(max_length=20)),
                ('status', models.CharField(verbose_name='Status', max_length=1, choices=[('A', 'Agendado'), ('F', 'Finalizado')])),
                ('observação', models.CharField(max_length=100)),
            ],
        ),
    ]
