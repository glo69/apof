# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 18:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_restaurant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='rating_description',
            field=models.CharField(default=datetime.datetime(2016, 3, 14, 18, 2, 38, 644557, tzinfo=utc), max_length=512),
            preserve_default=False,
        ),
    ]
