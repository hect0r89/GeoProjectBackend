# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0003_auto_20170606_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='radius',
            field=models.IntegerField(default=150, verbose_name='Radio'),
        ),
    ]
