# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secknowledgemodel',
            name='horizontal_image',
            field=models.BooleanField(default=False),
        ),
    ]
