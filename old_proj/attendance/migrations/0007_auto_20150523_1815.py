# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20150514_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_attendance',
            name='present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='meeting_attendance',
            name='present',
            field=models.BooleanField(default=False),
        ),
    ]
