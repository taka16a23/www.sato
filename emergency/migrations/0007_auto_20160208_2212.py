# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 13:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0006_auto_20160208_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergency',
            name='published_from',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 8, 22, 12, 14, 434961), help_text='\u516c\u958b\u3092\u9078\u629e\u3059\u308b\u3068\u3001\u3053\u3053\u3067\u8a2d\u5b9a\u3057\u305f\u65e5\u6642\u307e\u3067\u306f\u516c\u958b\u3055\u308c\u307e\u305b\u3093', verbose_name='\u516c\u958b\u958b\u59cb'),
        ),
        migrations.AlterField(
            model_name='emergency',
            name='status',
            field=models.BooleanField(choices=[(False, '\u4e0b\u66f8\u304d'), (True, '\u516c\u958b\u3059\u308b')], default=True, help_text='\u4e0b\u66f8\u304d\u3092\u9078\u629e\u3059\u308b\u3068\u3001\u30b5\u30a4\u30c8\u306e\u7ba1\u7406\u30e6\u30fc\u30b6\u30fc\u306e\u307f\u304c\u898b\u3089\u308c\u308b\u72b6\u614b\u306b\u306a\u308a\u307e\u3059\u3002'),
        ),
    ]