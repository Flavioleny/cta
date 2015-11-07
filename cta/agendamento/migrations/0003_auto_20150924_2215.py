# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0002_auto_20150924_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='dataagendamento',
            new_name='dataagendamento_ag',
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='dataatendimento',
            new_name='dataatendimento_ag',
        ),
    ]
