# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_member_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(default='NA', max_length=250, verbose_name='Adresse'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='mobile',
            field=models.IntegerField(default=123456789, verbose_name='T\xe9l. mobile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(default=123456789, verbose_name='T\xe9l. fixe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='prefix',
            field=models.IntegerField(default=10, verbose_name='Pr\xe9fix', choices=[(10, b'+352'), (11, b'+32'), (13, b'+49'), (12, b'+33')]),
            preserve_default=True,
        ),
    ]
