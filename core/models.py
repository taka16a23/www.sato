#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timesince import timesince

import datetime


class TimeStampModel(models.Model):
    r"""TimeStampModel

    TimeStampModel is a models.Model.
    Responsibility:
    """
    class Meta:
        abstract = True

    created = models.DateTimeField(null=True, editable=False)
    modified = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        now = datetime.datetime.now()
        self.updated = now
        if not self.id:
            self.modified = now
        super(TimeStampModel, self).save(*args, **kwargs)


DISPLAY_STATUS_DRAFT = 1
DISPLAY_STATUS_PUBLISHED = 2
DISPLAY_STATUS_CHOICES = (
    (DISPLAY_STATUS_PUBLISHED, u'公開'),
    (DISPLAY_STATUS_DRAFT, u'下書き'),
)


def base_concrete_model(abstract, instance):
    """
    Used in methods of abstract models to find the super-most concrete
    (non abstract) model in the inheritance chain that inherits from the
    given abstract model. This is so the methods in the abstract model can
    query data consistently across the correct concrete model.

    Consider the following::

        class Abstract(models.Model)

            class Meta:
                abstract = True

            def concrete(self):
                return base_concrete_model(Abstract, self)

        class Super(Abstract):
            pass

        class Sub(Super):
            pass

        sub = Sub.objects.create()
        sub.concrete() # returns Super

    In actual Mezzanine usage, this allows methods in the ``Displayable`` and
    ``Orderable`` abstract models to access the ``Page`` instance when
    instances of custom content types, (eg: models that inherit from ``Page``)
    need to query the ``Page`` model to determine correct values for ``slug``
    and ``_order`` which are only relevant in the context of the ``Page``
    model and not the model of the custom content type.
    """
    for cls in reversed(instance.__class__.__mro__):
        if issubclass(cls, abstract) and not cls._meta.abstract:
            return cls
    return instance.__class__


class DisplayableModel(TimeStampModel):
    r"""DisplayableModel

    DisplayableModel is a TimeStampModel.
    Responsibility:
    """
    class Meta:
        abstract = True

    status = models.IntegerField(
        u'ステータス',
        choices=DISPLAY_STATUS_CHOICES,
        default=DISPLAY_STATUS_PUBLISHED,
        help_text=u'下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。')

    publish_date = models.DateTimeField(
        u'公開開始',
        blank=True, null=True, db_index=True,
        help_text=u'公開を選択すると、ここで設定した日時までは公開されません')
    expiry_date = models.DateTimeField(
        u'有効期限',
        help_text=u'公開を選択すると、ここで設定した日時以降は公開されません',
        blank=True, null=True)

    def save(self, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        if self.publish_date is None:
            self.publish_date = datetime.datetime.now()
        super(DisplayableModel, self).save(**kwargs)

    def publish_date_since(self, ):
        r"""SUMMARY

        publish_date_since()

        @Return:

        @Error:
        """
        return timesince(self.publish_date)

    def get_next_by_publish_date(self, ):
        r"""SUMMARY

        get_next_by_publish_date()

        @Return:

        @Error:
        """
        concrete_model = base_concrete_model(DisplayableModel, self)
        nexts = concrete_model.objects.published().filter(
            publish_date__gt=self.publish_date).order_by('publish_date')
        if nexts:
            return nexts[0]
        return False

    def get_previous_by_publish_date(self, ):
        r"""SUMMARY

        get_previous_by_publish_date()

        @Return:

        @Error:
        """
        concrete_model = base_concrete_model(DisplayableModel, self)
        prevs = concrete_model.objects.published().filter(
            publish_date__lt=self.publish_date).order_by('-publish_date')
        if prevs:
            return prevs[0]
        return False



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
