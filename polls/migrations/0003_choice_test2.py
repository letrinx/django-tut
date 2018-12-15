# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='test2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
