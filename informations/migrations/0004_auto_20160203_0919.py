# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 00:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0003_auto_20160203_0916'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Informations',
            new_name='Information',
        ),
    ]