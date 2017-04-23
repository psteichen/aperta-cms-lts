# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20140921_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='desc',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
