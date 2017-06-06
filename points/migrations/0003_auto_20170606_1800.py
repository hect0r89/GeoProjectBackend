# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_auto_20170604_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='device_id',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Id dispositivo'),
        ),
        migrations.AddField(
            model_name='point',
            name='rating',
            field=models.FloatField(blank=True, null=True, verbose_name='Puntuación'),
        ),
    ]
