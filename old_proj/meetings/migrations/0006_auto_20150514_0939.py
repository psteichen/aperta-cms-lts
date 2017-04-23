# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import meetings.models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0005_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='attachement',
        ),
        migrations.AddField(
            model_name='meeting',
            name='report',
            field=models.FileField(upload_to=meetings.models.rename_report, null=True, verbose_name=b'Compte rendu', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='meeting',
            field=models.ForeignKey(to='meetings.Meeting'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.ForeignKey(verbose_name=b'Lieu de Rencontre', to='locations.Location'),
        ),
    ]
