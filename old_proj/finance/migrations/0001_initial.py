# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import finance.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20150514_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankExtract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=4)),
                ('num', models.IntegerField()),
                ('scan', models.FileField(upload_to=finance.models.rename_scan)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('type', models.IntegerField(choices=[(0, 'Cotisation'), (1, 'Avance'), (2, 'Activit\xe9'), (3, 'Don')])),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('recipient', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('invoice', models.ForeignKey(to='finance.Invoice')),
                ('sender', models.ForeignKey(to='members.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
