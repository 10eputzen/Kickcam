# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-20 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_analysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
