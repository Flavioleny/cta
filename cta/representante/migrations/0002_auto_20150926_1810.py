# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('representante', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='representante',
            options={'verbose_name': 'Representante', 'verbose_name_plural': 'Representante'},
        ),
    ]
