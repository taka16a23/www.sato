# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secknowledgemodel',
            name='image_status',
            field=models.IntegerField(choices=[(1, '\u7e26'), (2, '\u6a2a')], default=1, verbose_name='\u753b\u50cf\u306e\u72b6\u614b'),
        ),
    ]
