# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjetivoVisita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=20)),
            ],
        ),
    ]
