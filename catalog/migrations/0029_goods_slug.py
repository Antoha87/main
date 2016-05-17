# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 12:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
from slugify import slugify
import uuid



class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_remove_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='slug',
            field=models.SlugField(default=slugify(uuid.uuid4()), max_length=200, unique=True, verbose_name='\u0427\u041f\u0423'),
            preserve_default=False,
        ),
    ]
