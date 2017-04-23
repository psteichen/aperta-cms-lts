# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attachement',
            field=models.FileField(upload_to=b'events', null=True, verbose_name=b'Notice d\xc3\xa9taill\xc3\xa9e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(verbose_name=b'Lieu de Rencontre', blank=True, to='locations.Location', null=True),
        ),
    ]
