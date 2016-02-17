#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from lib.utils import get_context


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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
