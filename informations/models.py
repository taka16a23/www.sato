# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.
INFO_CATEGORIES = (
    (1, u'重要'),
    (2, u'お知らせ'),
    (3, u'防犯'),
    (4, u'ご報告'),
    (5, u'行事'),
    (6, u'募集'),
    (7, u'更新'),
)


class Information(models.Model):
    r"""Information

    Informations is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'タイトル', max_length=200, blank=False)
    ctime = models.DateTimeField(u'作成日時', auto_now_add=True, blank=False)
    pub_date = models.DateTimeField(u'公開日時', blank=False, default=datetime.now())
    category = models.IntegerField(u'お知らせの種類', choices=INFO_CATEGORIES, blank=False, default=2)
    url = models.URLField('URL', max_length=200, blank=False)
    publish = models.BooleanField(u'公開する', default=True)

    class Meta:
        verbose_name = u'お知らせ'
        verbose_name_plural = u'お知らせ'

    def __unicode__(self):
        return self.title
