# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0006_auto_20150925_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendamento',
            options={'verbose_name': 'Agendamento', 'verbose_name_plural': 'Agendamento'},
        ),
        migrations.AddField(
            model_name='agendamento',
            name='dataagendamento_ag',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 18, 10, 29, 172935, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agendamento',
            name='dataatendimento_ag',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 18, 10, 45, 382565, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
