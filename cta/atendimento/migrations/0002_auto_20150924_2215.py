# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='dataatendimento',
            new_name='dataatendimento_at',
        ),
    ]
