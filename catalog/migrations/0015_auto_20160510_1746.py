# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_imagegalery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='location',
            field=models.ManyToManyField(to='catalog.Location', verbose_name='\u041c\u0435\u0441\u0442\u043e\u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430'),
        ),
    ]