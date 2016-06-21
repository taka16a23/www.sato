#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import redirect

# Register your models here.

@admin.site.register_view('docs', u'使い方説明書')
def documents(request, *args, **kwargs):
    """SUMMARY

    documents(request, *args, **kwargs)

    @Arguments:
    - `request`:
    - `args`:
    - `kwargs`:

    @Return:

    @Error:
    """
    return redirect('/docs/')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
