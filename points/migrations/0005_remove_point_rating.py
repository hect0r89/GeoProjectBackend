# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0004_auto_20170606_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='rating',
        ),
    ]
