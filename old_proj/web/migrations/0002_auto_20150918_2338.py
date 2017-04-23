# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='index',
            field=models.ForeignKey(verbose_name="Page d'index", to='web.Page'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Cat\xe9gorie'),
        ),
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='page',
            name='last_update',
            field=models.DateField(verbose_name='Derni\xe8re mise \xe0 jour'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(unique=True, verbose_name='URL'),
        ),
    ]
