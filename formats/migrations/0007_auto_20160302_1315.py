# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 13:15
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formats', '0006_auto_20160301_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherformat',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='\u8aac\u660e'),
        ),
        migrations.AlterField(
            model_name='satoformat',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='\u8aac\u660e'),
        ),
        migrations.AlterField(
            model_name='staffformat',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='\u8aac\u660e'),
        ),
    ]
