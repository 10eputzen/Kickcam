# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-24 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Table',
        ),
    ]
