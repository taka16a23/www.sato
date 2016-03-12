#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""util -- DESCRIPTION

"""
from publish.models import ActivityPostModel, DocumentModel, NewsPostModel
from security.models import EmergencyEntryModel
from BeautifulSoup import BeautifulSoup

import about

import datetime

def displayable_uniq_year(model):
    r"""SUMMARY

    displayable_uniq_year(model)

    @Arguments:
    - `model`:

    @Return:

    @Error:
    """
    return [d.year for d in model.objects.published().datetimes(
        'publish_date', 'year')]


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
    news_uniq_years = displayable_uniq_year(NewsPostModel)
    if not now.year in news_uniq_years:
        news_uniq_years.append(now.year)
    news_uniq_years.sort()
    context['news_uniq_years'] = news_uniq_years
    # activity
    activity_uniq_years = displayable_uniq_year(ActivityPostModel)
    if not now.year in activity_uniq_years:
        activity_uniq_years.append(now.year)
    activity_uniq_years.sort()
    context['activity_uniq_years'] = activity_uniq_years
    # board
    board_uniq_years = displayable_uniq_year(DocumentModel)
    if not now.year in board_uniq_years:
        board_uniq_years.append(now.year)
    board_uniq_years.sort()
    context['board_uniq_years'] = board_uniq_years
    return context


def get_plaintext(text):
    r"""SUMMARY

    get_plaintext(text)

    @Arguments:
    - `text`:

    @Return:

    @Error:
    """
    soup = BeautifulSoup(unicode(text))
    [s.extract() for s in soup('script')]
    return u''.join([s.replace('&nbsp;', '') for s in soup.findAll(text=True)])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# util.py ends here
