#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity -- DESCRIPTION

"""

from BeautifulSoup import BeautifulSoup

from django.db import models
from django.utils.safestring import mark_safe

from core.models import DisplayableModel
from core.managers import DisplayableManager, DisplayableQuerySet
from ckeditor_uploader.fields import RichTextUploadingField


class ActivityPostQuerySet(DisplayableQuerySet):
    r"""ActivityPostQuerySet

    ActivityPostQuerySet is a DisplayableQuerySet.
    Responsibility:
    """
    def by_tagname(self, tagname):
        r"""SUMMARY

        by_tagname(tagname)

        @Arguments:
        - `tagname`:

        @Return:

        @Error:
        """
        return self.filter(tags__name=tagname)


class ActivityPostManager(DisplayableManager):
    r"""ActivityPostManager

    ActivityPostManager is a DisplayableManager.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return ActivityPostQuerySet(self.model)


class TagModel(models.Model):
    r"""TagModel

    TagModel is a models.Model.
    Responsibility:
    """
    name = models.CharField(
        u'タグ', unique=True, max_length=200, blank=False, null=False)

    def __unicode__(self):
        return self.name


class ActivityPostModel(DisplayableModel):
    r"""ActivityPostModel

    ActivityPostModel is a models.Model.
    Responsibility:
    """
    objects = ActivityPostManager()

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
    tags = models.ManyToManyField(
        TagModel,
        help_text=mark_safe('当てはまる項目をすべて選んでください<br>'),
        blank=True, related_name="tagging")

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
        super(ActivityPostModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity.py ends here
