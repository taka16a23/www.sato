#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""index -- DESCRIPTION

"""
from django.shortcuts import render_to_response
from django.template import RequestContext

from lib.utils import get_context


def security_view(request):
    r"""SUMMARY

    security_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    return render_to_response(
        'security/index.html', context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# index.py ends here
