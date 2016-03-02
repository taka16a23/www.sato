#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity -- DESCRIPTION

"""

from BeautifulSoup import BeautifulSoup
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

from core.models import DisplayableModel
from core.managers import DisplayableManager
from publish.models.news import NewsPostModel


class ActivityPostModel(DisplayableModel):
    r"""ActivityPostModel

    ActivityPostModel is a models.Model.
    Responsibility:
    """
    objects = DisplayableManager()

    class Meta:
        verbose_name = u'活動報告'
        verbose_name_plural = u'活動報告'

    title = models.CharField(u'題名', max_length=200)
    body = RichTextUploadingField(
        u'本文',
        help_text=u'入力ボックスの横幅が改行の大体の目安です',
        config_name='activity',
        blank=True, null=True)
    description = models.TextField(u'記事の説明', blank=True, null=True)
    # news = models.ForeignKey(NewsPostModel, null=True)

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
        # if self.news:
            # self.news.publish_date = self.publish_date
            # self.news.expiry_date = self.expiry_date
            # self.news.save()
        super(ActivityPostModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity.py ends here
