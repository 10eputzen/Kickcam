# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_activity_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='happy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='sql',
            field=models.CharField(blank=True, default='', max_length=4000),
        ),
    ]
