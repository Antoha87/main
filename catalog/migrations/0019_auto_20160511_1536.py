# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20160510_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='collection',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='goods',
            name='currence',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0412\u0430\u043b\u044e\u0442\u0430 \u0442\u043e\u0432\u0430\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='goods',
            name='model',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c \u0442\u043e\u0432\u0430\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='goods',
            name='torg',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0422\u043e\u0440\u0433\u043e\u0432\u043e\u0435 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
    ]
