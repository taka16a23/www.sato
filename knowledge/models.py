# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
IMAGE_STATUS = ((True, u'縦'),
              (False, u'横'),)


class SecKnowledgeModel(models.Model):
    r"""SecKnowledgeModel

    SecKnowledgeModel is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'タイトル', max_length=255)
    description = models.TextField(u'説明文', blank=True)
    url = models.URLField('URL', max_length=200, blank=False)
    thumbnail = models.ImageField(
        u'サムネイル',
        upload_to='knowledge/',
        blank=True, null=True)
    image_status = models.BooleanField(
        u'画像の状態',
        choices=IMAGE_STATUS,
        default=True)
    sortid = models.IntegerField(
        u'並び番号',
        help_text=u'サイトで昇順に並びます',
        default=100)
    publish = models.BooleanField(u'公開する', default=True)

    class Meta:
        verbose_name = u'防災予備知識'
        verbose_name_plural = u'防災予備知識'

    def __unicode__(self):
        return self.title
