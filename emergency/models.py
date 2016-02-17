#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from core.models import DisplayableModel
from core.managers import DisplayableManager


class EmergencyEntryModel(DisplayableModel):
    r"""EmergencyEntryModel

    EmergencyEntryModel is a DisplayableModel.
    Responsibility:
    """
    objects = DisplayableManager()

    title = models.CharField(u'タイトル', max_length=200, blank=False, null=False)
    body = models.TextField(u'本文', null=True)

    class Meta:
        verbose_name = u'緊急情報'
        verbose_name_plural = u'緊急情報'

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
