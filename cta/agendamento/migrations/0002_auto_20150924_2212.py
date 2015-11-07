# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='dataagendamento',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='dataatendimento',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
