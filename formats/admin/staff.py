#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""staff -- DESCRIPTION

"""
from django.contrib import admin

from formats.models import StaffFormat
from adminsortable2.admin import SortableAdminMixin


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
# staff.py ends here
