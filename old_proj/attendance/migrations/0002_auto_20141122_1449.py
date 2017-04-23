# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20141114_0131'),
        ('events', '0001_initial'),
        ('members', '0007_member_user'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('present', models.BooleanField()),
                ('event', models.ForeignKey(to='events.Event')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting_Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('present', models.BooleanField()),
                ('meeting', models.ForeignKey(to='meetings.Meeting')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='event',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='member',
        ),
        migrations.DeleteModel(
            name='Attendance',
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
