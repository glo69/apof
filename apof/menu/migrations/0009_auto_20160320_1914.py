# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20160320_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='dish',
            field=models.CharField(max_length=128),
        ),
    ]
