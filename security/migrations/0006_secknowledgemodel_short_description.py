# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0005_emergencyentrymodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='secknowledgemodel',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='\u6982\u8981'),
        ),
    ]