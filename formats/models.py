#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ckeditor.fields import RichTextField

from BeautifulSoup import BeautifulSoup

# Create your models here.
class SatoFormat(models.Model):
    r"""SatoFormat

    SatoFormat is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'書式名', max_length=255, blank=False)
    description = RichTextField(u'概要', config_name='simple', blank=True)
    short_description = models.TextField(u'概要', blank=True, null=True)
    file = models.FileField(u'PDF', upload_to='formats', blank=True)
    form = models.URLField(u'フォームアドレス', max_length=200, blank=True)
    sortid = models.IntegerField(
        u' ',
        help_text=u'サイトで昇順に並びます',
        default=0,
        blank=False,
        null=False,
        db_index=True)
    publish = models.BooleanField(u'公開する', default=True)

    class Meta:
        verbose_name = u'里自治会向け関係書式'
        verbose_name_plural = u'里自治会向け関係書式'
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
        super(SatoFormat, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class OtherFormat(models.Model):
    r"""OtherFormat

    OtherFormat is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'書式名', max_length=255, blank=False)
    description = RichTextField(u'概要', config_name='simple', blank=True)
    short_description = models.TextField(u'概要', blank=True, null=True)
    url = models.URLField(u'掲載URL', max_length=200, blank=True)
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
        verbose_name = u'自治体等関係書式'
        verbose_name_plural = u'自治体等関係書式'
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
        super(OtherFormat, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class StaffFormat(models.Model):
    r"""StaffFormat

    StaffFormat is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'書式名', max_length=255, blank=False)
    description = RichTextField(u'概要', config_name='simple', blank=True)
    short_description = models.TextField(u'概要', blank=True, null=True)
    file = models.FileField(u'ファイル', upload_to='formats', blank=True)
    sortid = models.IntegerField(
        u' ',
        help_text=u'サイトで昇順に並びます',
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    class Meta:
        verbose_name = u'役員用関係書式'
        verbose_name_plural = u'役員用関係書式'
        ordering = ['sortid', ]

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
