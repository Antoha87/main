# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-14 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('price', models.IntegerField(verbose_name='\u0426\u0435\u043d\u0430')),
                ('quantity', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('total_price', models.IntegerField(verbose_name='\u0412\u0441\u0435\u0433\u043e')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(editable=False, max_length=100)),
                ('delivery', models.TextField(blank=True, max_length=250, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u0418\u0442\u043e\u0433\u043e')),
                ('status', models.IntegerField(choices=[(1, '\u041f\u0440\u0438\u043d\u044f\u0442'), (2, '\u041e\u043f\u043b\u0430\u0447\u0435\u043d'), (3, '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d'), (4, '\u0417\u0430\u043a\u0440\u044b\u0442')], default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('price', models.IntegerField(verbose_name='\u0426\u0435\u043d\u0430')),
                ('quantity', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('total_price', models.IntegerField(verbose_name='\u0412\u0441\u0435\u0433\u043e')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.Order', verbose_name='\u0417\u0430\u043a\u0430\u0437')),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
    ]
