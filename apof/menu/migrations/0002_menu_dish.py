# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 20:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='dish',
            field=models.CharField(default=datetime.datetime(2016, 3, 6, 20, 45, 30, 169542, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
