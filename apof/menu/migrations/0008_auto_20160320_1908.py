# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='restaurant',
            field=models.CharField(max_length=128),
        ),
    ]