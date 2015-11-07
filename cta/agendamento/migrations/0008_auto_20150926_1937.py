# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0007_auto_20150926_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='dataatendimento_ag',
            field=models.DateTimeField(),
        ),
    ]
