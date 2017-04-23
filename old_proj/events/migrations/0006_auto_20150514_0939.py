# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attachement',
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(verbose_name=b'Lieu', to='locations.Location'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='sent',
            field=models.DateTimeField(),
        ),
    ]
