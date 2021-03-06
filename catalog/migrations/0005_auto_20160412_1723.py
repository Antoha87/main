# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20160412_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='city',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='region',
        ),
        migrations.RemoveField(
            model_name='goodsvariation',
            name='price_gramm',
        ),
        migrations.RemoveField(
            model_name='goodsvariation',
            name='price_product',
        ),
        migrations.RemoveField(
            model_name='goodsvariation',
            name='size',
        ),
        migrations.RemoveField(
            model_name='goodsvariation',
            name='weight',
        ),
        migrations.AlterField(
            model_name='options',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.GoodsVariation', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0438\u0435 \u043e\u043f\u0446\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432'),
        ),
    ]
