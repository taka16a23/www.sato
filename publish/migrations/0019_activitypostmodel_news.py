# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0018_auto_20160302_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitypostmodel',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='publish.NewsPostModel'),
        ),
    ]
