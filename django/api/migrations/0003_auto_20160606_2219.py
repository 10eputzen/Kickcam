# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160606_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replay',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
