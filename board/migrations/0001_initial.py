# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-06 22:05
from __future__ import unicode_literals

import board.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u30bf\u30a4\u30c8\u30eb')),
                ('file', models.FileField(upload_to=board.models.get_file_path, validators=[board.models.validate_file_pdf])),
                ('publish_date', models.DateField(default=datetime.date.today, help_text='\u30b0\u30eb\u30fc\u30d7\u5206\u3051\u3068\u4e26\u3073\u9806\u306e\u57fa\u6e96\u3068\u306a\u308a\u307e\u3059\u3002', verbose_name='\u516c\u958b\u65e5')),
                ('publish', models.BooleanField(default=True, verbose_name='\u516c\u958b\u3059\u308b')),
            ],
            options={
                'verbose_name': '\u56de\u89a7\u677f',
                'verbose_name_plural': '\u56de\u89a7\u677f',
            },
        ),
    ]
