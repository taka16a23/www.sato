#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.query import QuerySet
from django.db.models import Q

from core.managers import ManagerAbstract
from sato.settings import STATIC_URL

import datetime
import urlparse


EVENT_CONFIRMED_STATUS = 1
EVENT_TENTATIVE_STATUS = 2
EVENT_CANCELLED_STATUS = 3

EVENT_STATUS = ((EVENT_CONFIRMED_STATUS, 'confirmed'),
                (EVENT_TENTATIVE_STATUS, 'tentative'),
                (EVENT_CANCELLED_STATUS, 'cancelled'), )

EVENT_STATUS_DICT = {x[1]: x[0] for x in EVENT_STATUS}

GARBAGE_IMGS = {u'紙ごみ': urlparse.urljoin(STATIC_URL, 'images/paper.jpg'),
                u'燃やせるごみ': urlparse.urljoin(STATIC_URL, 'images/combustibles.jpg'),
                u'透明びん、茶色びん': urlparse.urljoin(STATIC_URL, 'images/bottles.jpg'),
                u'プラ容器包装': urlparse.urljoin(STATIC_URL, 'images/plastics.jpg'),
                u'ペットボトル': urlparse.urljoin(STATIC_URL, 'images/PET.jpg'),
                u'燃やせないごみ': urlparse.urljoin(STATIC_URL, 'images/incombustibles.jpg'),
                u'かん': urlparse.urljoin(STATIC_URL, 'images/cans.jpg'),
}


class EventQuerySet(QuerySet):
    r"""EventQuerySet

    EventQuerySet is a QuerySet.
    Responsibility:
    """
    def confirmed(self, ):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        return self.filter(status=EVENT_CONFIRMED_STATUS)

    def between_date(self, start, end):
        r"""SUMMARY

        between_date(start, end)

        @Arguments:
        - `start`:
        - `end`:

        @Return:

        @Error:
        """
        if end < start:
            start = end
        return self.filter(date__gte=start, date__lte=end)


class EventManager(ManagerAbstract):
    r"""EventManager

    EventManager is a .
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return EventQuerySet(self.model)


class GarbageEvent(models.Model):
    r"""GarbageEvent

    GarbageEvent is a models.Model.
    Responsibility:
    """
    objects = EventManager()

    gid = models.CharField(max_length=1024, unique=True)
    summary = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    status = models.IntegerField(
        choices=EVENT_STATUS, default=EVENT_CONFIRMED_STATUS)

    def __unicode__(self):
        return self.summary

    def url_of_image(self, ):
        r"""SUMMARY

        url_of_image()

        @Return:

        @Error:
        """
        return GARBAGE_IMGS.get(self.summary, '')


class MainEventQuerySet(EventQuerySet):
    r"""MainEventQuerySet

    MainEventQuerySet is a models.Model.
    Responsibility:
    """
    def between_events(self, mindate, maxdate):
        r"""SUMMARY

        @Arguments:
        - `mindate`:
        - `maxdate`:

        @Return:

        between_events(mindate, maxdate)

        @Error:

        予定のタイプは4種類
        1. start と end が mindate と maxdate の範囲内
        2. start が 範囲内 end が範囲外
        3. start が 範囲外 end が範囲内
        4. start と end が範囲外

        1と2の取得方法が mindate<=start<=maxdate
        3の取得方法が mindate<=end<=maxdate
        4の取得方法が start<=mindate<=end & start<=maxdate<=end
        で取得する。
        """
        return self.filter(
            Q(start__gte=mindate, start__lte=maxdate) # 1,2
            |Q(end__gte=mindate, end__lte=maxdate) # 3
            |Q(start__lte=mindate, end__gte=mindate) # 4
            &Q(start__lte=maxdate, end__gte=maxdate)
        )


class MainEventManager(EventManager):
    r"""MainEventManager

    MainEventManager is a models.Manager.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return MainEventQuerySet(self.model)


class MainEvent(models.Model):
    r"""MainEvent

    MainEvent is a models.Model.
    Responsibility:
    """
    objects = MainEventManager()

    gid = models.CharField(max_length=1024, unique=True)
    summary = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    url = models.URLField(null=True, blank=True)
    status = models.IntegerField(
        choices=EVENT_STATUS, default=EVENT_CONFIRMED_STATUS)

    def __unicode__(self):
        return self.summary

    def is_today_start(self, ):
        r"""SUMMARY

        is_today_start()

        @Return:

        @Error:
        """
        now = datetime.datetime.now()
        return self.start.date() == now.date()


class HallEvent(models.Model):
    r"""HallEvent

    HallEvent is a models.Model.
    Responsibility:
    """
    objects = MainEventManager()

    gid = models.CharField(max_length=1024, unique=True)
    summary = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(null=True)
    url = models.URLField(null=True, blank=True)
    status = models.IntegerField(
        choices=EVENT_STATUS, default=EVENT_CONFIRMED_STATUS)

    def __unicode__(self):
        return self.summary

    def is_today_start(self, ):
        r"""SUMMARY

        is_today_start()

        @Return:

        @Error:
        """
        now = datetime.datetime.now()
        return self.start.date() == now.date()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
