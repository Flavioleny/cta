# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0005_auto_20150924_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='dataagendamento_ag',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='dataatendimento_ag',
        ),
    ]
