#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from publish.models import DocumentModel, ActivityPostModel, NewsPostModel
from lib.utils import get_context


def board_view(request):
    r"""SUMMARY

    board(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    now = context['now']
    year = request.GET.get('year')
    if year is None or not year.isdigit() or not 2010 <= int(year) <= 2050:
        year = now.year
    context['year'] = year
    start = datetime.datetime(int(year), 1, 1)
    end = start + relativedelta(years=1) - relativedelta(minutes=1)
    context['board_list'] = (DocumentModel
                             .objects
                             .published()
                             .range_by_publish_date(start, end)
                             .order_by('-publish_date'))
    return render_to_response(
        'board/index.html', context, context_instance=RequestContext(request))




def activity_view(request):
    r"""SUMMARY

    activity_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    id_ = request.GET.get('id', None)
    # example "/activity?id=1"
    if id_:
        try:
            context['activity_post'] = ActivityPostModel.objects.get(id=id_)
        except ObjectDoesNotExist as err:
            print(err)
            return Http404
        return render_to_response(
            'activity/detail.html',
            context, context_instance=RequestContext(request))
    # example "/activity?year=2016"
    year = request.GET.get('year', None)
    now = context['now']
    if year is None or not year.isdigit() or not 2010 <= int(year) <= 2050:
        year = now.year
    context['year'] = year
    start = datetime.datetime(int(year), 1, 1)
    end = start + relativedelta(years=1) - relativedelta(minutes=1)
    publishings = (ActivityPostModel.objects
                   .published()
                   .range_by_publish_date(start, end)
                   .order_by('-publish_date'))
    context['activities'] = publishings
    return render_to_response(
        'activity/index.html',
        context, context_instance=RequestContext(request))


def news_view(request):
    r"""SUMMARY

    news_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    now = context['now']
    year = request.GET.get('year')
    if year is None or not year.isdigit() or not 2010 <= int(year) <= 2050:
        year = now.year
    context['year'] = year
    start = datetime.datetime(int(year), 1, 1)
    end = start + relativedelta(years=1) - relativedelta(minutes=1)
    context['newsList'] = (NewsPostModel
                             .objects
                             .published()
                             .range_by_publish_date(start, end)
                             .order_by('-publish_date'))
    return render_to_response(
        'news/index.html', context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
