#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""index -- DESCRIPTION

"""
from django.shortcuts import render_to_response
from django.template import RequestContext

from base.utils import get_context
from publish.models import NewsPostModel


def security_view(request):
    r"""SUMMARY

    security_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    context['newsList'] = (NewsPostModel
                           .objects
                           .published()
                           .list_security()
                           .list_security())
    return render_to_response(
        'security/index.html', context, context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# index.py ends here
