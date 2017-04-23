# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150514_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='attachement',
            field=models.FileField(upload_to=events.models.rename_attach, null=True, verbose_name=b'Annexe(s)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
