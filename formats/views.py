#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from formats.models import SatoFormat, OtherFormat
from django.template import RequestContext
from base.utils import get_context
from formats.forms import HallBookingForm
from django.http import HttpResponseRedirect
from django import forms

import datetime


# Create your views here.
def formats_view(request):
    r"""SUMMARY

    formats_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    context['satoformats'] = SatoFormat.objects.filter(
        publish=True).order_by('sortid')
    context['otherformats'] = OtherFormat.objects.filter(
        publish=True).order_by('sortid')
    return render_to_response(
        'formats/index.html', context, context_instance=RequestContext(request))


def form_hallbooking_view(request):
    r"""SUMMARY

    form_hallbooking_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    if request.method == 'POST':
        form = HallBookingForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/about/thankyou/')
    else:
        form = HallBookingForm()
    context['hallBookingForm'] = form
    return render_to_response(
        'formats/hallbooking/index.html',
        context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
