# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('category', models.IntegerField(choices=[(1, '\u91cd\u8981'), (2, '\u304a\u77e5\u3089\u305b'), (3, '\u9632\u72af'), (4, '\u3054\u5831\u544a'), (5, '\u884c\u4e8b'), (6, '\u52df\u96c6'), (7, '\u66f4\u65b0')])),
                ('url', models.URLField()),
                ('publish', models.BooleanField(default=True)),
            ],
        ),
    ]
