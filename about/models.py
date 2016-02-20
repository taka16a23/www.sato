#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.query import QuerySet

from core.managers import ManagerAbstract


class ContactPostModel(models.Model):
    r"""ContactModel

    ContactModel is a models.Model.
    Responsibility:
    """
    name = models.CharField(u'お名前', max_length=50, blank=False, null=False)
    email = models.EmailField(
        u'メールアドレス',
        max_length=100, blank=False, null=False)
    body = models.TextField(u'内容', blank=False, null=False)
    # for admins
    created = models.DateTimeField(u'投稿日', auto_now=True)
    finished = models.BooleanField(u'処理済', default=False)

    class Meta:
        verbose_name = u'情報提供・お問い合わせ項目'
        verbose_name_plural = u'情報提供・お問い合わせ項目'

    def __unicode__(self):
        return self.name


FAQ_STATUS_DRAFT = 1
FAQ_STATUS_PUBLISHED = 2
FAQ_STATUS_CHOICES = (
    (FAQ_STATUS_DRAFT, u'下書き'),
    (FAQ_STATUS_PUBLISHED, u'公開'),
)


class FAQQuerySet(QuerySet):
    r"""FAQQuerySet

    FAQQuerySet is a QuerySet.
    Responsibility:
    """
    def published(self, ):
        r"""SUMMARY

        published()

        @Return:

        @Error:
        """
        return self.filter(status=FAQ_STATUS_PUBLISHED)


class FAQManager(ManagerAbstract):
    r"""FAQManager

    FAQManager is a models.Manager.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return FAQQuerySet(self.model)


class QAModel(models.Model):
    r"""FAQEntryModel

    QAModel is a models.Model.
    Responsibility:
    """
    objects = FAQManager()

    question = models.CharField(u'質問', max_length=255)
    answer = models.TextField(u'回答', )
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        u'ステータス',
        choices=FAQ_STATUS_CHOICES,
        default=FAQ_STATUS_PUBLISHED,
        help_text=u'下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。')

    class Meta:
        verbose_name = u'よくある質問'
        verbose_name_plural = u'よくある質問'

    def __unicode__(self):
        return self.question



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
