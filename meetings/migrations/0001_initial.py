# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import meetings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=5000, null=True)),
                ('attachement', models.FileField(blank=True, null=True, upload_to=meetings.models.rename_attach, verbose_name='Annexe(s)')),
                ('sent', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invitee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nom')),
                ('email', models.EmailField(max_length=254)),
                ('type', models.IntegerField(choices=[(0, 'Invité'), (1, "Membre d'un autre club"), (2, 'Conférencier'), (3, 'Would-Be')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numéro')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('when', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Heure de début')),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('report', models.FileField(blank=True, null=True, upload_to=meetings.models.rename_report, verbose_name='Compte rendu')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Location', verbose_name='Lieu de Rencontre')),
            ],
        ),
        migrations.AddField(
            model_name='invitee',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Meeting'),
        ),
        migrations.AddField(
            model_name='invitee',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Meeting'),
        ),
    ]
