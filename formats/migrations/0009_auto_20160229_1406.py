# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 14:06
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formats', '0008_auto_20160229_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherformat',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='\u6982\u8981'),
        ),
        migrations.AlterField(
            model_name='satoformat',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='\u6982\u8981'),
        ),
    ]
