#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from activity.models import PostModel


@admin.register(PostModel)
class ActivityPostAdmin(admin.ModelAdmin):
    r"""PostAdmin

    PostAdmin is a admin.ModelAdmin.
    Responsibility:
    """

    list_display = ('title', 'status', 'publish_date', 'expiry_date', 'description')
    list_display_links = ("title",)
    list_editable = ('status', )
    ordering = ('-modified', )
    exclude = ('description', )
    radio_fields = {"status": admin.HORIZONTAL}
    date_hierarchy = 'publish_date'
    list_filter = ('status', 'publish_date', 'expiry_date', )

    fieldsets = ((None, {
        "fields": ["title", "status", ("publish_date", "expiry_date"), 'body'],
    }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
