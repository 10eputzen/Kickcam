# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20160521_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='analysis',
            field=models.IntegerField(blank=True),
        ),
    ]
