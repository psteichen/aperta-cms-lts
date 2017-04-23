# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'actif'), (1, b'honoraire'), (2, b'aspirant (wouldbe)'), (3, b'inactif (standby)')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
