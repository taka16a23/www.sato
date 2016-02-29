# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 15:03
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0003_auto_20160229_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('modified', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, '\u4e0b\u66f8\u304d'), (2, '\u516c\u958b')], default=2, help_text='\u4e0b\u66f8\u304d\u3092\u9078\u629e\u3059\u308b\u3068\u3001\u30b5\u30a4\u30c8\u306e\u7ba1\u7406\u30e6\u30fc\u30b6\u30fc\u306e\u307f\u304c\u898b\u3089\u308c\u308b\u72b6\u614b\u306b\u306a\u308a\u307e\u3059\u3002', verbose_name='\u30b9\u30c6\u30fc\u30bf\u30b9')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text='\u516c\u958b\u3092\u9078\u629e\u3059\u308b\u3068\u3001\u3053\u3053\u3067\u8a2d\u5b9a\u3057\u305f\u65e5\u6642\u307e\u3067\u306f\u516c\u958b\u3055\u308c\u307e\u305b\u3093', null=True, verbose_name='\u516c\u958b\u958b\u59cb')),
                ('expiry_date', models.DateTimeField(blank=True, help_text='\u516c\u958b\u3092\u9078\u629e\u3059\u308b\u3068\u3001\u3053\u3053\u3067\u8a2d\u5b9a\u3057\u305f\u65e5\u6642\u4ee5\u964d\u306f\u516c\u958b\u3055\u308c\u307e\u305b\u3093', null=True, verbose_name='\u6709\u52b9\u671f\u9650')),
                ('title', models.CharField(max_length=200, verbose_name='\u30bf\u30a4\u30c8\u30eb')),
                ('body', ckeditor.fields.RichTextField(null=True, verbose_name='\u672c\u6587')),
            ],
            options={
                'verbose_name': '\u7dca\u6025\u60c5\u5831',
                'verbose_name_plural': '\u7dca\u6025\u60c5\u5831',
            },
        ),
    ]