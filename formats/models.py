#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SatoFormat(models.Model):
    r"""SatoFormat

    SatoFormat is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'書式名', max_length=255, blank=False)
    description = RichTextField(u'概要', config_name='simple', blank=True)
    file = models.FileField(u'PDF', upload_to='formats', blank=True)
    form = models.URLField(u'フォームアドレス', max_length=200, blank=True)
    sortid = models.IntegerField(
        u'並び番号',
        help_text=u'サイトで昇順に並びます',
        default=100)
    publish = models.BooleanField(u'公開する', default=True)

    class Meta:
        verbose_name = u'里自治会関係書式'
        verbose_name_plural = u'里自治会関係書式'

    def __unicode__(self):
        return self.title


class OtherFormat(models.Model):
    r"""OtherFormat

    OtherFormat is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'書式名', max_length=255, blank=False)
    description = RichTextField(u'概要', config_name='simple', blank=True)
    url = models.URLField(u'掲載URL', max_length=200, blank=True)
    sortid = models.IntegerField(
        u'並び番号',
        help_text=u'サイトで昇順に並びます',
        default=100)
    publish = models.BooleanField(u'公開する', default=True)

    class Meta:
        verbose_name = u'自治体等関係書式'
        verbose_name_plural = u'自治体等関係書式'

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
