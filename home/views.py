#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from publish.models import NewsPostModel
from lib.utils import get_context
from home.models import GarbageEvent, MainEvent, HallEvent

import datetime
from calendar import (MONDAY, TUESDAY, WEDNESDAY, THURSDAY,
                      FRIDAY, SATURDAY, SUNDAY)

WEEKDAY_JDIC = {MONDAY: u'月',
                TUESDAY: u'火',
                WEDNESDAY: u'水',
                THURSDAY: u'木',
                FRIDAY: u'金',
                SATURDAY: u'土',
                SUNDAY: u'日'}

PAST_COUNTS = 7

class Day(object):
    r"""Day

    Day is a object.
    Responsibility:
    """
    def __init__(self, date):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._date = date

    @property
    def year(self, ):
        r"""SUMMARY

        year()

        @Return:

        @Error:
        """
        return self._date.year

    @property
    def month(self, ):
        r"""SUMMARY

        month()

        @Return:

        @Error:
        """
        return self._date.month

    @property
    def day(self, ):
        r"""SUMMARY

        day()

        @Return:

        @Error:
        """
        return self._date.day

    @property
    def week(self, ):
        r"""SUMMARY

        week()

        @Return:

        @Error:
        """
        return WEEKDAY_JDIC.get(self._date.weekday())


def home_view(request):
    r"""SUMMARY

    home_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context(emergency=True)
    now = context['now']
    context['today'] = Day(now)
    context['newsList'] = NewsPostModel.objects.latest_by_days(PAST_COUNTS)
    context['todayGarbageCollection'] = GarbageEvent.objects.filter(
        date=now)
    start = datetime.datetime.combine(now, datetime.time.min)
    end = datetime.datetime.combine(now, datetime.time.max)
    context['todaySchedules'] = MainEvent.objects.between_events(
        start, end).confirmed().order_by('start')
    context['todayHallBooking'] = HallEvent.objects.between_events(
        start, end).confirmed().order_by('start')
    tomorrow = now + datetime.timedelta(1)
    start, end = start + datetime.timedelta(1), end + datetime.timedelta(1)
    context['tomorrowGarbageCollection'] = GarbageEvent.objects.filter(
        date=tomorrow)
    context['tomorrowSchedules'] = MainEvent.objects.between_events(
        start, end).confirmed().order_by('start')
    return render_to_response(
        'home/home.html', context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
