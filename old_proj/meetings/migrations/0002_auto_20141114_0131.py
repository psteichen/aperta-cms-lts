# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitation',
            old_name='event',
            new_name='meeting',
        ),
    ]
