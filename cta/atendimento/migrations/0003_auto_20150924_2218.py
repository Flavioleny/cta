# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0002_auto_20150924_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='dataatendimento_at',
            field=models.DateTimeField(),
        ),
    ]
