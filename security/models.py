#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import DisplayableModel
from core.managers import DisplayableManager
from ckeditor.fields import RichTextField

from BeautifulSoup import BeautifulSoup


class EmergencyEntryModel(DisplayableModel):
    r"""EmergencyEntryModel

    EmergencyEntryModel is a DisplayableModel.
    Responsibility:
    """
    objects = DisplayableManager()

    title = models.CharField(u'タイトル', max_length=200, blank=False, null=False)
    body = RichTextField(u'本文', config_name='simple', null=True)
    description = models.TextField(u'概要', blank=True, null=True)

    class Meta:
        verbose_name = u'緊急情報'
        verbose_name_plural = u'緊急情報'

    def save(self, *args, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        text = u''
        try:
            text = u''.join(BeautifulSoup(self.body).findAll(text=True))
        except Exception as err:
            # TODO: (Atami) [2016/02/17]
            print(err)
        self.description = text[:300]
        super(EmergencyEntryModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


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
    short_description = models.TextField(u'概要', blank=True, null=True)
    url = models.URLField('URL', max_length=200, blank=False)
    thumbnail = models.ImageField(
        u'サムネイル',
        upload_to='knowledge/',
        blank=True, null=True)
    # image_status = models.IntegerField(
    #     u'画像の状態',
    #     choices=IMAGE_STATUS,
    #     default=IMAGE_VERTICAL)
    sortid = models.IntegerField(
        u' ',
        help_text=u'サイトで昇順に並びます',
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )
    publish = models.BooleanField(u'公開する', default=True)

    class Meta:
        verbose_name = u'防災予備知識'
        verbose_name_plural = u'防災予備知識'
        ordering = ['sortid', ]

    def save(self, *args, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        text = u''
        try:
            text = u''.join(BeautifulSoup(self.description).findAll(text=True))
        except Exception as err:
            # TODO: (Atami) [2016/02/17]
            print(err)
        self.short_description = text[:300]
        super(SecKnowledgeModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
