# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-07-02 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0004_auto_20170419_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='rx_update_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Time Ended'),
        ),
    ]