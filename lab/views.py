#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from datetime import datetime


# Create your views here.
def lab_view(request):
    r"""SUMMARY

    lab_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response('lab/index.html', context)

def server_view(request):
    r"""SUMMARY

    server_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    return render_to_response('lab/server.html', context)


def weather_view(request):
    """SUMMARY

    weather_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    now = datetime.now()
    if now.month in (2, 3, 4):
        context['weather_urls'] = ['http://weathernews.jp/pollen/#//c=0', ]
    if now.month in (7, 8, 9, 10):
        context['weather_urls'] = ['http://weathernews.jp/typhoon/']
    return render_to_response('lab/weather.html', context)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
