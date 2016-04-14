# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Goods', verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0438\u0435 \u043e\u043f\u0446\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432')),
            ],
            options={
                'verbose_name': '\u041e\u043f\u0446\u0438\u044e',
                'verbose_name_plural': '\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0438\u0435 \u043e\u043f\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='OptionsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438')),
                ('value', models.CharField(max_length=100, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0438\u0435 \u043e\u043f\u0446\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432',
                'verbose_name_plural': '\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043e\u043f\u0446\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430',
            },
        ),
        migrations.DeleteModel(
            name='SpecialOffer',
        ),
        migrations.AddField(
            model_name='options',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.OptionsList', verbose_name='\u041e\u043f\u0446\u0438\u044f'),
        ),
    ]
