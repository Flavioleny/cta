# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedor'},
        ),
    ]
