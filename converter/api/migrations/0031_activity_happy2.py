# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-30 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20160530_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='happy2',
            field=models.BooleanField(default=False),
        ),
    ]
