# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20141122_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_attendance',
            name='present',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='meeting_attendance',
            name='present',
            field=models.NullBooleanField(),
        ),
    ]
