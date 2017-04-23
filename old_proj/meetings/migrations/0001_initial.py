# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=5000)),
                ('sent', models.DateTimeField(blank=True,null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name=b'Titre')),
                ('num', models.IntegerField(serialize=False, verbose_name=b'Num\xc3\xa9ro', primary_key=True)),
                ('when', models.DateField(verbose_name=b'Date')),
                ('time', models.TimeField(verbose_name=b'Heure de d\xc3\xa9but')),
                ('deadline', models.DateField(verbose_name=b'Deadline')),
                ('location', models.ForeignKey(verbose_name=b'Lieu', to='locations.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='invitation',
            name='event',
            field=models.ForeignKey(to='meetings.Meeting'),
            preserve_default=True,
        ),
    ]
