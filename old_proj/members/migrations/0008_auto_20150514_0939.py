# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Date de fin', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Pr\xe9nom'),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='member',
            name='start_date',
            field=models.DateField(verbose_name='Date de d\xe9but'),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Statut', choices=[(0, b'actif'), (1, b'honoraire'), (2, b'aspirant (wouldbe)'), (3, b'inactif (standby)')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(verbose_name='Utilisateur', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='desc',
            field=models.CharField(max_length=500, null=True, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Date de fin', blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='start_date',
            field=models.DateField(verbose_name='Date de d\xe9but'),
        ),
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titre'),
        ),
    ]
