# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

STATUS = ((False, u'下書き'),
          (True, u'公開する'))


# Create your models here.
class Emergency(models.Model):
    r"""Emergency

    Emergency is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'タイトル', max_length=30, blank=False, null=False)
    description = models.TextField(u'本文', null=True)
    published_from = models.DateTimeField(
        u'公開開始',
        help_text=u'公開を選択すると、ここで設定した日時までは公開されません',
        default=datetime.now())
    expires_on = models.DateTimeField(
        u'有効期限',
        help_text=u'公開を選択すると、ここで設定した日時以降は公開されません',
        blank=True, null=True)
    status = models.BooleanField(
        help_text=u'下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。',
        choices=STATUS,
        default=True)

    class Meta:
        verbose_name = u'緊急情報'
        verbose_name_plural = u'緊急情報'

    def __unicode__(self):
        return self.title
