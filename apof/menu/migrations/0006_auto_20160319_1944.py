# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 19:44
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20160317_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='open_hours',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=datetime.datetime(2016, 3, 19, 19, 43, 46, 863016, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='close_hour',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery_time',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='open_hour',
            field=models.CharField(default=9, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]