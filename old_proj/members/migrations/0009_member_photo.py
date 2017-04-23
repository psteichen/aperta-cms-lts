# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20150514_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(upload_to=members.models.rename_photo, null=True, verbose_name='Photo', blank=True),
            preserve_default=True,
        ),
    ]
