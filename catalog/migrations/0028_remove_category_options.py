# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_auto_20160513_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='options',
        ),
    ]