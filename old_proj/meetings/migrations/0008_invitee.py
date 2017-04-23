# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20150514_0939'),
        ('meetings', '0007_invitation_attachement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='Pr\xe9nom')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=75)),
                ('type', models.IntegerField(default=0, choices=[(0, 'Invit\xe9'), (1, "Membre d'un autre club"), (2, 'Conf\xe9rencier'), (3, 'Would-Be')])),
                ('meeting', models.ForeignKey(to='meetings.Meeting')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
