#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin

from formats.admin._sato import SatoFormatAdmin
from formats.admin.other import OtherFormatAdmin
from formats.admin.staff import StaffFormatAdmin
from formats.models import SatoFormat, OtherFormat, StaffFormat


__all__ = ['SatoFormatAdmin', 'OtherFormatAdmin', 'StaffFormatAdmin', ]


admin.site.register(SatoFormat, SatoFormatAdmin)
admin.site.register(OtherFormat, OtherFormatAdmin)
admin.site.register(StaffFormat, StaffFormatAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
