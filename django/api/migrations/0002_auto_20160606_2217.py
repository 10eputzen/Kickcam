# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 22:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='replay',
            options={'ordering': ('date',)},
        ),
        migrations.AddField(
            model_name='replay',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]