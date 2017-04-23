# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('attendance', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='event_attendance',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
        ),
        migrations.AddField(
            model_name='etom',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='etom',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
        ),
        migrations.AlterUniqueTogether(
            name='meeting_attendance',
            unique_together=set([('member', 'meeting')]),
        ),
        migrations.AlterUniqueTogether(
            name='event_attendance',
            unique_together=set([('member', 'event')]),
        ),
    ]
