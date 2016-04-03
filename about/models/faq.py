#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""faq -- DESCRIPTION

"""
from django.db import models
from django.db.models.query import QuerySet

from ckeditor.fields import RichTextField

from core.managers import ManagerAbstract
from base.functions import get_plaintext


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
    answer = RichTextField(u'回答', config_name='simple')
    description = models.TextField(u'概要', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    sortid = models.IntegerField(
        u' ',
        help_text=u'サイトで昇順に並びます',
        default=0,
        blank=False,
        null=False,
        db_index=True,)
    status = models.IntegerField(
        u'ステータス',
        choices=FAQ_STATUS_CHOICES,
        default=FAQ_STATUS_PUBLISHED,
        help_text=u'下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。')

    def save(self, *args, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        text = u''
        try:
            text = get_plaintext(self.answer)
        except Exception as err:
            # TODO: (Atami) [2016/02/17]
            print(err)
        self.description = text[:300]
        super(QAModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'よくある質問'
        verbose_name_plural = u'よくある質問'
        ordering = ['sortid', ]

    def __unicode__(self):
        return self.question



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# faq.py ends here
