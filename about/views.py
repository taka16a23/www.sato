#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from base.utils import get_context

from about.forms import ContactPostForm, HallBookingForm, ChildrenPostForm
from about.models import QAModel
import datetime


def about_view(request):
    r"""SUMMARY

    about_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    return HttpResponseRedirect("/about/solve")


def group_view(request):
    r"""SUMMARY

    group_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    return render_to_response(
        'group/index.html', context, context_instance=RequestContext(request))


def solve_view(request):
    r"""SUMMARY

    solve_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    form = ContactPostForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.send_notify(
            u'里自治会受付番号:{0:05}番,情報提供・お問合わせがありました'
            .format(obj.id))
        obj.send_accept(u'里自治会受付完了通知')
        return HttpResponseRedirect('/about/thankyou/', )
    if request.method == 'POST':
        form = ContactPostForm(request.POST)
        context['anchor'] = 'contact'
    else:
        form = ContactPostForm()
    context['contactForm'] = form
    context['qalist'] = QAModel.objects.published()
    return render_to_response(
        'about/solve/index.html',
        context,
        context_instance=RequestContext(request))


def thankyou(request):
    r"""SUMMARY

    thankyou(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    return render_to_response(
        'about/solve/thankyou.html', context,
        context_instance=RequestContext(request))


def rule(request):
    r"""SUMMARY

    rule(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    return render_to_response(
        'about/rule/index.html', context, context_instance=RequestContext(request))


def greeding(request):
    r"""SUMMARY

    greeding(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    return render_to_response(
        'about/index.html', context, context_instance=RequestContext(request))


def form_hall_view(request):
    """SUMMARY

    form_hall_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    form = HallBookingForm(request.POST)
    if form.is_valid():
        accept_num = datetime.datetime.now().strftime('%g%m%d%H%M%f')
        if form.send_accept(accept_num) != 0:
            if form.send_notify(accept_num) != 0:
                return HttpResponseRedirect('/about/thankyou/')
    if request.method == 'POST':
        form = HallBookingForm(request.POST)
    else:
        form = HallBookingForm()
    context = get_context()
    context['hallBookingForm'] = form
    return render_to_response(
        'about/hall/index.html',
        context, context_instance=RequestContext(request))


def children(request):
    """SUMMARY

    children()

    @Return:

    @Error:
    """
    form = ChildrenPostForm(request.POST)
    if form.is_valid():
        accept_num = datetime.datetime.now().strftime('%g%m%d%H%M%f')
        if form.send_accept(accept_num) != 0:
            if form.send_notify(accept_num) != 0:
                return HttpResponseRedirect('/about/thankyou/')
    if request.method == 'POST':
        form = ChildrenPostForm(request.POST)
    else:
        form = ChildrenPostForm()
    context = get_context()
    context['hallBookingForm'] = form
    return render_to_response(
        'about/children/index.html', context,
        context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
