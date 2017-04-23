# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import meetings.models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_auto_20150514_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='attachement',
            field=models.FileField(upload_to=meetings.models.rename_attach, null=True, verbose_name=b'Annexe(s)', blank=True),
            preserve_default=True,
        ),
    ]
