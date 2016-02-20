#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

from lib.utils import get_context
from activity.models import PostModel

import datetime
from dateutil.relativedelta import relativedelta


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
            context['activity_post'] = PostModel.objects.get(id=id_)
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
    publishings = (PostModel.objects
                   .published()
                   .range_by_publish_date(start, end)
                   .order_by('-publish_date'))
    context['activities'] = publishings
    return render_to_response(
        'activity/index.html',
        context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
