# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150514_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='sent',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
