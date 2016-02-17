#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from formats.models import SatoFormat, OtherFormat
from django.template import RequestContext
from lib.utils import get_context


# Create your views here.
def formats(request):
    r"""SUMMARY

    formats(request)

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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
