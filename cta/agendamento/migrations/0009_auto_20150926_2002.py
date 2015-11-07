# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0008_auto_20150926_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='dataagendamento_ag',
            new_name='dataagendamento',
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='dataatendimento_ag',
            new_name='dataatendimento',
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='observação',
            new_name='observacao',
        ),
    ]
