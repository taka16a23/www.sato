#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""contact -- DESCRIPTION

"""
from django.db import models
from django.db.models.query import QuerySet
from django.core.mail import EmailMessage

from core.managers import ManagerAbstract
from core.models import TimeStampModel

from sato import settings
from about import PHONE_NUMBER


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


class ContactReceiverQuerySet(QuerySet):
    r"""ContactReceiverQuerySet

    ContactReceiverQuerySet is a QuerySet.
    Responsibility:
    """
    def active(self, ):
        r"""SUMMARY

        active()

        @Return:

        @Error:
        """
        return self.filter(models.Q(active=True))


class ContactReceiverManager(ManagerAbstract):
    r"""ContactReceiverManager

    ContactReceiverManager is a ManagerAbstract.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return ContactReceiverQuerySet(self.model)


class ContactReceiverModel(TimeStampModel):
    r"""ContactReceiverModel

    ContactReceiverModel is a models.Model.
    Responsibility:
    """
    objects = ContactReceiverManager()

    name = models.CharField(u'名前', max_length=50, blank=True, null=True)
    email = models.EmailField(
        u'メールアドレス', blank=False, null=False)
    active = models.BooleanField(u'受信する', default=True)

    class Meta(object):
        verbose_name = u'フォーム受取人'
        verbose_name_plural = u'フォーム受取人'

    def __unicode__(self):
        return self.name


UNTREATED_STATUS = 1
CONFIRMED_STATUS = 2
FINISHED_STATUS = 3

CONTACT_STATUS = ((UNTREATED_STATUS, '未処理'),
                  (CONFIRMED_STATUS, '確認済'),
                  (FINISHED_STATUS, '処理済'), )

CONTACT_STATUS_DICT = {x[1]: x[0] for x in CONTACT_STATUS}


class ContactedModel(TimeStampModel):
    r"""ContactedModel

    ContactedModel is a models.Model.
    Responsibility:
    """
    name = models.CharField(u'名前', max_length=50, blank=True, null=True)
    email = models.EmailField(
        u'メールアドレス', blank=False, null=False)
    status = models.IntegerField(
        choices=CONTACT_STATUS, default=UNTREATED_STATUS)
    body = models.TextField(u'内容', blank=True, null=True, )

    class Meta(object):
        verbose_name = u'申込み・問い合わせ一覧'
        verbose_name_plural = u'申込み・問い合わせ一覧'

    def send_notify(self, subject):
        r"""SUMMARY

        send_notify(subject)

        @Arguments:
        - `subject`:

        @Return:

        @Error:
        """
        emails = [x.email for x in ContactReceiverModel.objects.active()]
        msg = EmailMessage(
            subject=subject, body=self.body,
            from_email=settings.EMAIL_HOST_USER, bcc=emails)
        return msg.send()

    def send_accept(self, subject):
        r"""SUMMARY

        send_accept(subject)

        @Arguments:
        - `subject`:

        @Return:

        @Error:
        """
        body = u''
        body += u'受付番号【{}】\n'.format(self.id)
        body += u'以下の内容で受付ました。\n'
        body += u'３日以内にこちらから連絡がない場合は、電話番号: {} にて、ご連絡をお願いいたします。'.format(PHONE_NUMBER)
        body += u'------------------------------------\n'
        body += u'お名前: {}様'.format(self.name)
        body += u'\n'
        body += self.body
        body += u'\n\n'
        body += u'------------------------------------\n'
        body += u'里自治会'
        msg = EmailMessage(
            subject=subject, body=body,
            from_email=settings.EMAIL_HOST_USER, to=[self.email, ])
        return msg.send()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# contact.py ends here
