# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 13:12
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', ckeditor.fields.RichTextField(help_text='\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u0430\u043d\u043d\u0435\u0440\u0430', max_length=100, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', ckeditor.fields.RichTextField(help_text='\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0431\u0430\u043d\u043d\u0435\u0440\u0430', verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0431\u0430\u043d\u043d\u0435\u0440\u0430')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL \u0431\u0430\u043d\u043d\u0435\u0440\u0430')),
                ('activate', models.BooleanField(default=False, help_text='\u0410\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u044f \u0431\u0430\u043d\u043d\u0435\u0440\u0430', verbose_name='\u0410\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u044f')),
                ('deactivate', models.DateTimeField(help_text='\u0412\u0440\u0435\u043c\u044f \u0434\u0435\u0430\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0431\u0430\u043d\u043d\u0435\u0440\u0430', verbose_name='\u0414\u0435\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u044f \u0431\u0430\u043d\u043d\u0435\u0440\u0430')),
                ('img', sorl.thumbnail.fields.ImageField(help_text='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u0431\u0430\u043d\u043d\u0435\u0440\u0430', upload_to='uploads', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u0431\u0430\u043d\u043d\u0435\u0440\u0430')),
            ],
            options={
                'verbose_name': '\u0411\u0430\u043d\u043d\u0435\u0440',
                'verbose_name_plural': '\u0411\u0430\u043d\u043d\u0435\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='banner',
            name='index',
            field=models.ForeignKey(help_text='\u0411\u0430\u043d\u043d\u0435\u0440', on_delete=django.db.models.deletion.CASCADE, to='pages.Index', verbose_name='\u0411\u0430\u043d\u043d\u0435\u0440'),
        ),
    ]
