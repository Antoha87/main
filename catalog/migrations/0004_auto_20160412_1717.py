# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_geoip', '0001_initial'),
        ('catalog', '0003_auto_20160412_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='region', chained_model_field='region', default=2, on_delete=django.db.models.deletion.CASCADE, related_name='city_ads', to='django_geoip.City', verbose_name='\u0413\u043e\u0440\u043e\u0434'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='region',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='django_geoip.Region', verbose_name='\u0420\u0435\u0433\u0438\u043e\u043d'),
            preserve_default=False,
        ),
    ]
