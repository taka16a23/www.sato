#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from sato.settings import STATIC_URL
from formats.models import SatoFormat, OtherFormat


@admin.register(SatoFormat)
class SatoFormatAdmin(admin.ModelAdmin):
    r"""SatoFormatAdmin

    SatoFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'description', 'file', 'form', 'sortid', 'publish')
    list_editable = ('sortid', 'publish', )
    ordering = ('sortid', )

    class Media:
        js = (STATIC_URL + 'tiny_mce/tiny_mce.js',
              STATIC_URL + 'tiny_mce/simple_tiny_mce.js',)


@admin.register(OtherFormat)
class OtherFormatAdmin(admin.ModelAdmin):
    r"""OtherFormatAdmin

    OtherFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'description', 'sortid', 'publish')
    list_editable = ('sortid', 'publish', )
    ordering = ('sortid', )

    class Media:
        js = (STATIC_URL + 'tiny_mce/tiny_mce.js',
              STATIC_URL + 'tiny_mce/simple_tiny_mce.js',)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
