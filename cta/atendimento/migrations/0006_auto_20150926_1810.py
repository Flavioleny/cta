# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0005_remove_atendimento_dataatendimento_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atendimento',
            options={'verbose_name': 'Atendimento', 'verbose_name_plural': 'Atendimento'},
        ),
        migrations.AddField(
            model_name='atendimento',
            name='dataatendimento_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 18, 10, 58, 766635, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
