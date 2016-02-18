#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
