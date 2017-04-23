# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150514_0945'),
        ('members', '0008_auto_20150514_0939'),
        ('meetings', '0008_invitee'),
        ('attendance', '0007_auto_20150523_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtoM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yes_hash', models.CharField(max_length=250)),
                ('no_hash', models.CharField(max_length=250)),
                ('event', models.ForeignKey(to='events.Event')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MtoM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yes_hash', models.CharField(max_length=250)),
                ('no_hash', models.CharField(max_length=250)),
                ('meeting', models.ForeignKey(to='meetings.Meeting')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
