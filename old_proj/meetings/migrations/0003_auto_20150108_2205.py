# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20141114_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='sent',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
