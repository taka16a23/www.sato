#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


# Create your views here.

def easy_add_board_view(request):
    """SUMMARY

    easy_add_board_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'easy_add_board/index.html', context)


def publish_calendar_view(request):
    """SUMMARY

    publish_calendar_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'publish_calendar/index.html', context)


def easy_add_activity_view(request):
    """SUMMARY

    easy_add_activity_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'easy_add_activity/index.html', context)


def top_view(request):
    """SUMMARY

    top_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response(
        'docs_top/index.html', context)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
