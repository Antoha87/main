# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-14 14:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.RemoveField(
            model_name='client',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='client',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='client',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='middlename',
        ),
        migrations.RemoveField(
            model_name='client',
            name='register_date',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(default=datetime.datetime(2016, 7, 14, 14, 9, 32, 885000, tzinfo=utc), max_length=255, unique=True, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]