# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 17:44
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactedModel',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('modified', models.DateTimeField(editable=False, null=True)),
                ('contactedid', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='\u53d7\u4ed8\u756a\u53f7')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u540d\u524d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9')),
                ('status', models.IntegerField(choices=[(1, b'\xe6\x9c\xaa\xe5\x87\xa6\xe7\x90\x86'), (2, b'\xe7\xa2\xba\xe8\xaa\x8d\xe6\xb8\x88'), (3, b'\xe5\x87\xa6\xe7\x90\x86\xe6\xb8\x88')], default=1)),
                ('body', models.TextField(blank=True, null=True, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u7533\u8fbc\u307f\u30fb\u554f\u3044\u5408\u308f\u305b\u4e00\u89a7',
                'verbose_name_plural': '\u7533\u8fbc\u307f\u30fb\u554f\u3044\u5408\u308f\u305b\u4e00\u89a7',
            },
        ),
        migrations.CreateModel(
            name='ContactPostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u304a\u540d\u524d')),
                ('email', models.EmailField(max_length=100, verbose_name='\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9')),
                ('body', models.TextField(verbose_name='\u5185\u5bb9')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='\u6295\u7a3f\u65e5')),
                ('finished', models.BooleanField(default=False, verbose_name='\u51e6\u7406\u6e08')),
            ],
            options={
                'verbose_name': '\u60c5\u5831\u63d0\u4f9b\u30fb\u304a\u554f\u3044\u5408\u308f\u305b\u9805\u76ee',
                'verbose_name_plural': '\u60c5\u5831\u63d0\u4f9b\u30fb\u304a\u554f\u3044\u5408\u308f\u305b\u9805\u76ee',
            },
        ),
        migrations.CreateModel(
            name='ContactReceiverModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('modified', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u540d\u524d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9')),
                ('active', models.BooleanField(default=True, verbose_name='\u53d7\u4fe1\u3059\u308b')),
            ],
            options={
                'verbose_name': '\u30d5\u30a9\u30fc\u30e0\u53d7\u53d6\u4eba',
                'verbose_name_plural': '\u30d5\u30a9\u30fc\u30e0\u53d7\u53d6\u4eba',
            },
        ),
        migrations.CreateModel(
            name='QAModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='\u8cea\u554f')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='\u56de\u7b54')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u6982\u8981')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sortid', models.IntegerField(db_index=True, default=0, help_text='\u30b5\u30a4\u30c8\u3067\u6607\u9806\u306b\u4e26\u3073\u307e\u3059', verbose_name=' ')),
                ('status', models.IntegerField(choices=[(1, '\u4e0b\u66f8\u304d'), (2, '\u516c\u958b')], default=2, help_text='\u4e0b\u66f8\u304d\u3092\u9078\u629e\u3059\u308b\u3068\u3001\u30b5\u30a4\u30c8\u306e\u7ba1\u7406\u30e6\u30fc\u30b6\u30fc\u306e\u307f\u304c\u898b\u3089\u308c\u308b\u72b6\u614b\u306b\u306a\u308a\u307e\u3059\u3002', verbose_name='\u30b9\u30c6\u30fc\u30bf\u30b9')),
            ],
            options={
                'ordering': ['sortid'],
                'verbose_name': '\u3088\u304f\u3042\u308b\u8cea\u554f',
                'verbose_name_plural': '\u3088\u304f\u3042\u308b\u8cea\u554f',
            },
        ),
    ]
