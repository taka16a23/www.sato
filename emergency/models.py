# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Emergency(models.Model):
    r"""Emergency

    Emergency is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'タイトル', max_length=30, blank=False, null=False)
    mtime = models.DateTimeField(u'編集日', blank=False, default=datetime.now())
    description = models.TextField(u'本文', null=True)
    publish = models.BooleanField(u'公開する', default=True)

    class Meta:
        verbose_name = u'緊急情報'
        verbose_name_plural = u'緊急情報'

    def __unicode__(self):
        return self.title
