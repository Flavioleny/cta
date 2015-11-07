# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0007_auto_20150926_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='dataatendimento_at',
            new_name='dataatendimento',
        ),
    ]
