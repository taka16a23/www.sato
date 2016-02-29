#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

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


@admin.register(OtherFormat)
class OtherFormatAdmin(admin.ModelAdmin):
    r"""OtherFormatAdmin

    OtherFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'description', 'sortid', 'publish')
    list_editable = ('sortid', 'publish', )
    ordering = ('sortid', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
