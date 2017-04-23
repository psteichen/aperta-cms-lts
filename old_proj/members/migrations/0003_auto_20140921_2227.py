# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20140921_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='role',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='first_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='role',
            name='member',
            field=models.ForeignKey(default=None, to='members.Member'),
            preserve_default=False,
        ),
    ]
