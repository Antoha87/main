# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20160412_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionslist',
            name='value',
        ),
        migrations.AddField(
            model_name='options',
            name='value',
            field=models.CharField(default=1, max_length=100, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='options',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Goods', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0438\u0435 \u043e\u043f\u0446\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432'),
        ),
    ]
