#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from sato.settings import STATIC_URL
from activity.models import PostModel


@admin.register(PostModel)
class ActivityPostAdmin(admin.ModelAdmin):
    r"""PostAdmin

    PostAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    class Media:
        js = (STATIC_URL + 'tiny_mce/tiny_mce.js',
              STATIC_URL + 'tiny_mce/full_tiny_mce.js',)

    list_display = ('title', 'status', 'publish_date', 'expiry_date', 'description')
    list_editable = ('status', )
    ordering = ('-modified', )
    exclude = ('description', )
    radio_fields = {"status": admin.HORIZONTAL}
    list_filter = ('status', 'publish_date', 'expiry_date', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
