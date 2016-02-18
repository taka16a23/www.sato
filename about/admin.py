#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from about.models import ContactPostModel


@admin.register(ContactPostModel)
class ContactAdmin(admin.ModelAdmin):
    r"""ContactAdmin

    ContactAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('name', 'title', 'created', 'email', 'body',  'finished')
    list_editable = ('finished', )
    # radio_fields = {"finished": admin.HORIZONTAL}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
