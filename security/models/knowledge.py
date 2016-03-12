#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""knowledge -- DESCRIPTION

"""
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from base.functions import get_plaintext


# string for adminsortable2
IMAGE_VERTICAL = u'縦'
IMAGE_HORIZON = u'横'

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
    image_status = models.CharField(
        u'画像の状態',
        max_length=5,
        choices=IMAGE_STATUS,
        default=IMAGE_VERTICAL)
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
            text = get_plaintext(self.description)
        except Exception as err:
            # TODO: (Atami) [2016/02/17]
            print(err)
        self.short_description = text[:300]
        super(SecKnowledgeModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def is_vertical_image(self, ):
        r"""SUMMARY

        is_vertical_image()

        @Return:

        @Error:
        """
        return self.image_status == IMAGE_VERTICAL



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# knowledge.py ends here
