# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0004_auto_20150924_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='dataagendamento_ag',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='dataatendimento_ag',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
