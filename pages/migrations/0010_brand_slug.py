# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20160421_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True, verbose_name='\u0427\u041f\u0423'),
            preserve_default=False,
        ),
    ]
