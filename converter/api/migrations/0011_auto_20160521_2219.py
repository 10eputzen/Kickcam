# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20160521_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
