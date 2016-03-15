#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news -- DESCRIPTION

"""
import datetime
from dateutil.relativedelta import relativedelta

from django.template import RequestContext
from django.shortcuts import render_to_response

from publish.models import NewsPostModel
from base.utils import get_context


def news_view(request):
    """SUMMARY

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
    end = datetime.datetime.combine(
        datetime.datetime(int(year) + 1, 12, 31), datetime.time.max)
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
# news.py ends here
