# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Budget',
            new_name='Point',
        ),
    ]
