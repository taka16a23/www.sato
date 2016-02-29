#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import DisplayableModel
from core.managers import DisplayableManager
from ckeditor_uploader.fields import RichTextUploadingField


from BeautifulSoup import BeautifulSoup


class PostModel(DisplayableModel):
    r"""PostModel

    PostModel is a models.Model.
    Responsibility:
    """
    objects = DisplayableManager()

    class Meta:
        verbose_name = u'活動項目'
        verbose_name_plural = u'活動項目'

    title = models.CharField(u'題名', max_length=200)
    body = RichTextUploadingField(u'本文', blank=True, null=True)
    description = models.TextField(u'記事の説明', blank=True, null=True)

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
        super(PostModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
