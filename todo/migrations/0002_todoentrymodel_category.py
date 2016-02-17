# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoentrymodel',
            name='category',
            field=models.IntegerField(choices=[(1, 'feature'), (2, 'fix')], default=1),
        ),
    ]
