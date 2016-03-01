#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from formats.models import SatoFormat, OtherFormat, StaffFormat
from adminsortable2.admin import SortableAdminMixin


@admin.register(SatoFormat)
class SatoFormatAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""SatoFormatAdmin

    SatoFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'short_description', 'file', 'form', 'publish')
    list_editable = ('publish', )
    exclude = ['sortid', 'short_description', ]


@admin.register(OtherFormat)
class OtherFormatAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""OtherFormatAdmin

    OtherFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'short_description', 'publish')
    list_editable = ('publish', )
    exclude = ['sortid', 'short_description', ]


@admin.register(StaffFormat)
class StaffFormatAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""StaffFormatAdmin

    OtherFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'short_description', 'file', )
    exclude = ['sortid', 'short_description', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
