#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""other -- DESCRIPTION

"""
from django.contrib import admin

from formats.models import OtherFormat
from adminsortable2.admin import SortableAdminMixin


@admin.register(OtherFormat)
class OtherFormatAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""OtherFormatAdmin

    OtherFormatAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'short_description', 'publish')
    list_editable = ('publish', )
    exclude = ['sortid', 'short_description', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# other.py ends here
