# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_attendance',
            name='present',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='meeting_attendance',
            name='present',
            field=models.BooleanField(),
        ),
    ]
