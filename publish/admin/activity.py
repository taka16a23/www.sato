#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity -- DESCRIPTION

"""
from django.contrib import admin
from publish.models import ActivityPostModel


@admin.register(ActivityPostModel)
class ActivityPostAdmin(admin.ModelAdmin):
    r"""ActivityPostAdmin

    ActivityPostAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'status', 'publish_date', 'expiry_date', 'description')
    list_display_links = ('title', )
    list_editable = ('status', )
    ordering = ('-modified', )
    exclude = ('description', )
    radio_fields = {"status": admin.HORIZONTAL}
    date_hierarchy = 'publish_date'
    list_filter = ('status', 'publish_date', 'expiry_date', )

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = ((None, {
        'fields': ['title', ('publish_date', 'expiry_date'), 'body', 'status', ],
    }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity.py ends here
