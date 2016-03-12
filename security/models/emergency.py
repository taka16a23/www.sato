#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""emergency -- DESCRIPTION

"""
from __future__ import unicode_literals
from django.db import models

from core.models import DisplayableModel
from core.managers import DisplayableManager
from ckeditor.fields import RichTextField
from base.utils import get_plaintext


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
            text = get_plaintext(self.body)
        except Exception as err:
            # TODO: (Atami) [2016/02/17]
            print(err)
        self.description = text[:300]
        super(EmergencyEntryModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# emergency.py ends here
