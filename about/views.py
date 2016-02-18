#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from lib.utils import get_context

from about.forms import ContactPostForm


def about_view(request):
    r"""SUMMARY

    about_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    return render_to_response(
        'about/index.html', context, context_instance=RequestContext(request))


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


def contactform(request):
    context = get_context()
    form = ContactPostForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/contact/thankyou/')
    context['form'] = ContactPostForm()
    return render_to_response(
        'contact/index.html',
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
    return render_to_response('contact/thankyou.html', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
