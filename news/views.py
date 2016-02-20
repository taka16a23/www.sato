#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from lib.utils import get_context
from news.models import PostModel

import datetime
from dateutil.relativedelta import relativedelta


def view(request):
    r"""SUMMARY

    view(request)

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
    context['newsList'] = (PostModel
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
