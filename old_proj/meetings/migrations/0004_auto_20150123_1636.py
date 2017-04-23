# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_auto_20150108_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='deadline',
            field=models.DateTimeField(verbose_name=b'Deadline'),
        ),
    ]
