# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20140921_2233'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set([('member', 'start_date', 'end_date')]),
        ),
    ]
