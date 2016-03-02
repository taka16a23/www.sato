#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""util -- DESCRIPTION

"""
from publish.models import ActivityPostModel, DocumentModel, NewsPostModel
from security.models import EmergencyEntryModel
import about

import datetime


def get_context(emergency=False):
    r"""SUMMARY

    get_context()

    @Return:

    @Error:
    """
    context = {}
    if emergency:
        context['emergencies'] = EmergencyEntryModel.objects.published().order_by(
            '-publish_date')
    now = datetime.datetime.now()
    context['now'] = now
    # about
    context['about'] = about
    # news
    news_uniq_years = NewsPostModel.objects.published().uniq_fiscal_years()
    if not now.year in news_uniq_years:
        news_uniq_years.append(now.year)
    news_uniq_years.sort()
    context['news_uniq_years'] = news_uniq_years
    # activity
    activity_uniq_years = ActivityPostModel.objects.published().uniq_fiscal_years()
    if not now.year in activity_uniq_years:
        activity_uniq_years.append(now.year)
    activity_uniq_years.sort()
    context['activity_uniq_years'] = activity_uniq_years
    # board
    board_uniq_years = DocumentModel.objects.published().uniq_fiscal_years()
    if not now.year in board_uniq_years:
        board_uniq_years.append(now.year)
    board_uniq_years.sort()
    context['board_uniq_years'] = board_uniq_years
    return context



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# util.py ends here
