# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0003_auto_20150924_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='dataagendamento_ag',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='dataatendimento_ag',
            field=models.DateTimeField(),
        ),
    ]
