# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 23:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20160521_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='analysis',
        ),
    ]