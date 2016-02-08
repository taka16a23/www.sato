# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ContactModel(models.Model):
    r"""ContactModel

    ContactModel is a models.Model.
    Responsibility:
    """
    name = models.CharField(u'お名前', max_length=50, blank=False, null=False)
    email = models.EmailField(
        u'メールアドレス',
        max_length=70, blank=False, null=False)
    title = models.CharField(
        u'件名',
        max_length=200,
        help_text= u'要件名を記入してください',
        blank=False, null=False)
    body = models.TextField(u'内容', blank=False, null=False)
    # for admins
    created = models.DateTimeField(u'投稿日', auto_now=True)
    finished = models.BooleanField(u'処理済', default=False)

    class Meta:
        verbose_name = u'お問い合わせ'
        verbose_name_plural = u'お問い合わせ'

    def __unicode__(self):
        return self.title
