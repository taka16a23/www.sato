#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity -- DESCRIPTION

"""
import datetime
from dateutil.relativedelta import relativedelta

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from publish.models import ActivityPostModel
from base.utils import get_context


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
        if now.month in (1, 2, 3):
            year = int(year) - 1
    context['year'] = year
    publishings = (ActivityPostModel.objects
                   .published()
                   .by_fiscal_year(year)
                   .order_by('-publish_date'))
    context['activities'] = publishings
    return render_to_response(
        'activity/index.html',
        context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity.py ends here
