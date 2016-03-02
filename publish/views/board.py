#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""board -- DESCRIPTION

"""
import datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render_to_response
from django.template import RequestContext

from publish.models import DocumentModel
from base.utils import get_context


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
        if now.month in (1, 2, 3):
            year = int(year) - 1
    context['year'] = year
    # start = datetime.datetime(int(year), 1, 1)
    # end = start + relativedelta(years=1) - relativedelta(minutes=1)
    # context['board_list'] = (DocumentModel
                             # .objects
                             # .published()
                             # .range_by_publish_date(start, end)
                             # .order_by('-publish_date'))
    context['board_list'] = (DocumentModel
                             .objects
                             .published()
                             .by_fiscal_year(year)
                             .order_by('-publish_date'))
    return render_to_response(
        'board/index.html', context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# board.py ends here
