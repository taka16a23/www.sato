# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_qamodel_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qamodel',
            options={'ordering': ['sortid'], 'verbose_name': '\u3088\u304f\u3042\u308b\u8cea\u554f', 'verbose_name_plural': '\u3088\u304f\u3042\u308b\u8cea\u554f'},
        ),
        migrations.AddField(
            model_name='qamodel',
            name='sortid',
            field=models.IntegerField(db_index=True, default=0, help_text='\u30b5\u30a4\u30c8\u3067\u6607\u9806\u306b\u4e26\u3073\u307e\u3059', verbose_name=' '),
        ),
    ]
