# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0030_auto_20160517_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='menu_type',
            field=models.BooleanField(default=False, help_text='\u041f\u0440\u0438 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0439 \u0433\u0430\u043b\u043e\u0447\u043a\u0435 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043f\u0440\u043e\u0441\u0442\u043e\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0432 \u043c\u0435\u043d\u044e', verbose_name='\u0422\u0438\u043f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0434\u043b\u044f \u043c\u0435\u043d\u044e'),
        ),
    ]
