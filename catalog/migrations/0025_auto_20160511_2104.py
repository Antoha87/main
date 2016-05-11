# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_auto_20160511_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0426\u0432\u0435\u0442'),
        ),
        migrations.AddField(
            model_name='goods',
            name='gab',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0413\u0430\u0431\u0430\u0440\u0438\u0442\u044b'),
        ),
        migrations.AddField(
            model_name='goods',
            name='krat',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u041a\u0440\u0430\u0442\u043d\u043e\u0441\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='goods',
            name='post',
            field=models.CharField(max_length=100, null=True, verbose_name='\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a'),
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0422\u0438\u043f'),
        ),
        migrations.AddField(
            model_name='goods',
            name='ves',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0412\u0435\u0441'),
        ),
        migrations.AddField(
            model_name='goods',
            name='vid',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u0412\u0438\u0434'),
        ),
    ]
