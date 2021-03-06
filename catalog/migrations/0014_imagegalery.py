# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 14:02
from __future__ import unicode_literals

import catalog.models
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_goods_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGalery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=catalog.models.image_path, verbose_name='\u0424\u043e\u0442\u043e')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Goods', verbose_name='\u0424\u043e\u0442\u043e \u0433\u0430\u043b\u0435\u0440\u0435\u044f')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e',
            },
        ),
    ]
