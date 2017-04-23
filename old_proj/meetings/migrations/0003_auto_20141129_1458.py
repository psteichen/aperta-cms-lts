# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20141114_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='attachement',
            field=models.FileField(upload_to=b'meetings', null=True, verbose_name=b'Notice d\xc3\xa9taill\xc3\xa9e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='meeting',
            field=models.OneToOneField(to='meetings.Meeting'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.ForeignKey(verbose_name=b'Lieu de Rencontre', blank=True, to='locations.Location', null=True),
        ),
    ]
