# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import finance.models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20170803_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankextract',
            name='scan',
            field=models.FileField(default=0, upload_to=finance.models.rename_be_scan),
            preserve_default=False,
        ),
    ]