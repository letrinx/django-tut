# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_test2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='test',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='test2',
        ),
    ]
