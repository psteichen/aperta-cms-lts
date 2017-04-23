# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20140928_1505'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set([('member', 'title')]),
        ),
    ]
