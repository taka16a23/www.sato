# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0009_remove_activitypostmodel_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspostmodel',
            name='url',
            field=models.SlugField(help_text='http://sato.jp \u306b\u7d9a\u304fURL\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044\u3002(\u4f8b) /activity/id=1', max_length=200, verbose_name=b'URL'),
        ),
    ]
