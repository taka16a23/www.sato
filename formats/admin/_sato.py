#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sato -- DESCRIPTION

"""
from django.contrib import admin

from formats.models import SatoFormat
from adminsortable2.admin import SortableAdminMixin


class SatoFormatAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""SatoFormatAdmin

    SatoFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'short_description', 'file', 'form', 'publish')
    list_editable = ('publish', )
    exclude = ['sortid', 'short_description', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sato.py ends here
