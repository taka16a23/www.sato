# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0016_auto_20160302_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitypostmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text=b'\xe5\xbd\x93\xe3\x81\xa6\xe3\x81\xaf\xe3\x81\xbe\xe3\x82\x8b\xe9\xa0\x85\xe7\x9b\xae\xe3\x82\x92\xe3\x81\x99\xe3\x81\xb9\xe3\x81\xa6\xe9\x81\xb8\xe3\x82\x93\xe3\x81\xa7\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84<br\\>\xe8\xa4\x87\xe6\x95\xb0\xe9\x81\xb8\xe6\x8a\x9e\xe3\x81\x99\xe3\x82\x8b\xe3\x81\xa8\xe3\x81\x8d\xe3\x81\xab\xe3\x81\xaf Control \xe3\x82\xad\xe3\x83\xbc\xe3\x82\x92\xe6\x8a\xbc\xe3\x81\x97\xe3\x81\x9f\xe3\x81\xbe\xe3\x81\xbe\xe9\x81\xb8\xe6\x8a\x9e\xe3\x81\x97\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84\xe3\x80\x82Mac \xe3\x81\xa7\xe3\x81\xaf Command \xe3\x82\xad\xe3\x83\xbc\xe3\x82\x92\xe4\xbd\xbf\xe3\x81\xa3\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84', related_name='tagging', to='publish.TagModel'),
        ),
    ]