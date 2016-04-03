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
from about import PHONE_NUMBER, DEADLINE


ACCEPT_MSG = u"""
{0[name]} 様

里自治会です。入力を受け付けました。
受付番号は【{0[accept_num]}】です。
内容を確認後、ご連絡いたします。
{0[deadline]}以内にこちらから連絡がない場合は、電話番号: {0[phone]} にて、ご連絡をお願いいたします。

○ 以下の内容で受付しました --

お名前: {0[name]}
メールアドレス: {0[email]}
{0[body]}
--------------------------------------------

■本メールは自動配信しています。
■本メールにお心当たりがない場合は、メールを削除いただきますようお願いいたします。

◇電話でのお問合せ
里自治会 {0[phone]}
"""

NOTIFY_MSG = u"""
ホームページ訪問者から入力を受付ました。

受付番号は【{0[accept_num]}】

○ 以下の内容で受付しました --

お名前: {0[name]}
メールアドレス: {0[email]}
{0[body]}
--------------------------------------------

※必ず入力者と連絡をとってください。
  対応が遅れる場合はその旨の返答をしてください。

以下の管理ページへアクセスしステータスを変更してください。
http://taka16.no-ip.info/admin/about/contactedmodel/
"""


class ContactReceiverQuerySet(QuerySet):
    """ContactReceiverQuerySet

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
        verbose_name = u'問い合わせ受取人'
        verbose_name_plural = u'問い合わせ受取人'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        super(ContactReceiverModel, self).save(*args, **kwargs)


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
        u'処理状況',
        choices=CONTACT_STATUS, default=UNTREATED_STATUS)
    body = models.TextField(u'内容', blank=True, null=True, )

    def save(self, *args, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        super(ContactedModel, self).save(*args, **kwargs)

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
        content = {}
        content['accept_num'] = u'{0:05}'.format(self.id)
        content['name'] = self.name
        content['email'] = self.email
        content['body'] = self.body
        msg = EmailMessage(
            subject=subject, body=NOTIFY_MSG.format(content),
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
        content = {}
        content['accept_num'] = u'{0:05}'.format(self.id)
        content['name'] = self.name
        content['email'] = self.email
        content['body'] = self.body
        content['phone'] = PHONE_NUMBER
        content['deadline'] = DEADLINE
        msg = EmailMessage(
            subject=subject, body=ACCEPT_MSG.format(content),
            from_email=settings.EMAIL_HOST_USER, to=[self.email, ])
        return msg.send()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# contact.py ends here
