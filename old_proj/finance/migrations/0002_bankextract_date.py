# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankextract',
            name='date',
            field=models.DateField(default=datetime.date(2015, 11, 8), verbose_name=b'\xc3\xa9tat du'),
            preserve_default=False,
        ),
    ]
