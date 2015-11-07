# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0003_auto_20150924_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='dataatendimento_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
