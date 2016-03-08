# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 13:27
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtherFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u66f8\u5f0f\u540d')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='\u8aac\u660e')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='\u6982\u8981')),
                ('url', models.URLField(blank=True, verbose_name='\u63b2\u8f09URL')),
                ('sortid', models.IntegerField(db_index=True, default=0, help_text='\u30b5\u30a4\u30c8\u3067\u6607\u9806\u306b\u4e26\u3073\u307e\u3059', verbose_name=' ')),
                ('publish', models.BooleanField(default=True, verbose_name='\u516c\u958b\u3059\u308b')),
            ],
            options={
                'ordering': ['sortid'],
                'verbose_name': '\u81ea\u6cbb\u4f53\u7b49\u95a2\u4fc2\u66f8\u5f0f',
                'verbose_name_plural': '\u81ea\u6cbb\u4f53\u7b49\u95a2\u4fc2\u66f8\u5f0f',
            },
        ),
        migrations.CreateModel(
            name='SatoFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u66f8\u5f0f\u540d')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='\u8aac\u660e')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='\u6982\u8981')),
                ('file', models.FileField(blank=True, upload_to='formats', verbose_name='PDF')),
                ('form', models.URLField(blank=True, verbose_name='\u30d5\u30a9\u30fc\u30e0\u30a2\u30c9\u30ec\u30b9')),
                ('sortid', models.IntegerField(db_index=True, default=0, help_text='\u30b5\u30a4\u30c8\u3067\u6607\u9806\u306b\u4e26\u3073\u307e\u3059', verbose_name=' ')),
                ('publish', models.BooleanField(default=True, verbose_name='\u516c\u958b\u3059\u308b')),
            ],
            options={
                'ordering': ['sortid'],
                'verbose_name': '\u91cc\u81ea\u6cbb\u4f1a\u5411\u3051\u95a2\u4fc2\u66f8\u5f0f',
                'verbose_name_plural': '\u91cc\u81ea\u6cbb\u4f1a\u5411\u3051\u95a2\u4fc2\u66f8\u5f0f',
            },
        ),
        migrations.CreateModel(
            name='StaffFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u66f8\u5f0f\u540d')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='\u8aac\u660e')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='\u6982\u8981')),
                ('file', models.FileField(blank=True, upload_to='formats', verbose_name='\u30d5\u30a1\u30a4\u30eb')),
                ('sortid', models.IntegerField(db_index=True, default=0, help_text='\u30b5\u30a4\u30c8\u3067\u6607\u9806\u306b\u4e26\u3073\u307e\u3059', verbose_name=' ')),
            ],
            options={
                'ordering': ['sortid'],
                'verbose_name': '\u5f79\u54e1\u7528\u95a2\u4fc2\u66f8\u5f0f',
                'verbose_name_plural': '\u5f79\u54e1\u7528\u95a2\u4fc2\u66f8\u5f0f',
            },
        ),
    ]
