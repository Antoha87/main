# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20160510_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='category',
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ManyToManyField(to='catalog.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
    ]