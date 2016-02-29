#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
IMAGE_VERTICAL = 1
IMAGE_HORIZON = 2

IMAGE_STATUS = ((IMAGE_VERTICAL, u'縦'),
                (IMAGE_HORIZON, u'横'),)


class SecKnowledgeModel(models.Model):
    r"""SecKnowledgeModel

    SecKnowledgeModel is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'タイトル', max_length=255)
    description = RichTextField(u'説明文', config_name='simple', blank=True)
    url = models.URLField('URL', max_length=200, blank=False)
    thumbnail = models.ImageField(
        u'サムネイル',
        upload_to='knowledge/',
        blank=True, null=True)
    image_status = models.IntegerField(
        u'画像の状態',
        choices=IMAGE_STATUS,
        default=IMAGE_VERTICAL)
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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
