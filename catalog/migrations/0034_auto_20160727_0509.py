# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0033_auto_20160727_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='stock',
            field=models.CharField(blank=True, default=0, max_length=100, null=True, verbose_name='\u041e\u0441\u0442\u0430\u0442\u043e\u043a \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435'),
        ),
    ]