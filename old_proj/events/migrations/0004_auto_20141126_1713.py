# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20141126_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='event',
            field=models.OneToOneField(to='events.Event'),
        ),
    ]
