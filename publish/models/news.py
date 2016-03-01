#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news -- DESCRIPTION

"""
import datetime

from django.db import models

from core.models import DisplayableModel
from core.managers import DisplayableQuerySet, ManagerAbstract
from colorfield.fields import ColorField

NEWS_IMPORTANT = 1
NEWS_INFORMATION = 2
NEWS_SECURITY = 3
NEWS_ACTIVITY = 4
NEWS_WANTED = 5
NEWS_UPDATE = 6


NEWS_CATEGORIES = (
    (NEWS_IMPORTANT, u'重要'),
    (NEWS_INFORMATION, u'お知らせ'),
    (NEWS_SECURITY, u'防犯'),
    (NEWS_ACTIVITY, u'ご報告'),
    (NEWS_WANTED, u'募集'),
    (NEWS_UPDATE, u'更新'),
)

NEWS_CATEGORIES_DIC = {integer: name for integer, name in NEWS_CATEGORIES}

CATEGORY_CLASS_KEYS = {
    NEWS_IMPORTANT: 'categoryImportant',
    NEWS_INFORMATION: 'categoryInfo',
    NEWS_SECURITY: 'categorySecurity',
    NEWS_ACTIVITY: 'categoryReport',
    NEWS_WANTED: 'categoryWanted',
    NEWS_UPDATE: 'categoryUpdate',
}

MIN_NEWS_COUNTS = 8


class NewsCategoryModel(models.Model):
    r"""NewsCategoryModel

    NewsCategoryModel is a models.Model.
    Responsibility:
    """
    name = models.CharField(u'カテゴリー名',
                            max_length=8,
                            help_text=u'8文字以内',
                            null=False,
                            blank=False)
    fgcolor = ColorField(u'文字色', default='#ffffff')
    bgcolor = ColorField(u'背景色', default='#ff0000')
    sortid = models.IntegerField(
        u' ',
        help_text=u'サイトで昇順に並びます',
        default=0,
        blank=False,
        null=False,
        db_index=True)

    class Meta:
        verbose_name = u'お知らせカテゴリー'
        verbose_name_plural = u'お知らせカテゴリー'
        ordering = ['sortid', ]

    def __unicode__(self):
        return self.name



class NewsPostQuerySet(DisplayableQuerySet):
    r"""NewsPostQuerySet

    NewsPostQuerySet is a DisplayableQuerySet.
    Responsibility:
    """
    def latest_by_days(self, days, min_news_counts=MIN_NEWS_COUNTS):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        end = now = datetime.datetime.now()
        start = now - datetime.timedelta(days)
        news = self.published().order_by('-publish_date')[:min_news_counts]
        rangenews = self.range_by_publish_date(start, end).order_by('-publish_date')
        if len(news) < len(rangenews):
            return rangenews
        return news


class NewsPostManager(ManagerAbstract):
    r"""NewsPostManager

    NewsPostManager is a ManagerAbstract.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return NewsPostQuerySet(self.model)


class NewsPostModel(DisplayableModel):
    r"""NewsPostModel

    NewsPostModel is a DisplayableModel.
    Responsibility:
    """
    objects = NewsPostManager()

    title = models.CharField(u'タイトル', max_length=200, blank=False)
    category = models.ForeignKey(NewsCategoryModel, null=False)
    url = models.URLField('URL', max_length=200, blank=False)

    class Meta:
        verbose_name = u'お知らせ'
        verbose_name_plural = u'お知らせ'

    def __unicode__(self):
        return unicode(self.title)

    def as_class_key(self, ):
        r"""SUMMARY

        as_class_key()

        @Return:

        @Error:
        """
        return CATEGORY_CLASS_KEYS.get(self.category)

    def as_category_name(self, ):
        r"""SUMMARY

        as_category_name()

        @Return:

        @Error:
        """
        return NEWS_CATEGORIES_DIC.get(self.category, u'')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# news.py ends here
