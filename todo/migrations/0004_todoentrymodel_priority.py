# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20160216_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoentrymodel',
            name='priority',
            field=models.IntegerField(choices=[(5, 'high'), (10, 'normal'), (15, 'low')], default=10),
        ),
    ]
