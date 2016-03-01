#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from publish.models import DocumentModel, ActivityPostModel, NewsPostModel


@admin.register(DocumentModel)
class DocumentAdmin(admin.ModelAdmin):
    r"""DocumentAdmin

    DocumentAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'status', 'publish_date', 'expiry_date')
    list_editable = ('status', )
    ordering = ('-publish_date', )
    exclude = ('thumbnail', )
    radio_fields = {"status": admin.HORIZONTAL}

    class Media:
        css = {'all': ('css/admin_sato.css', ),}


@admin.register(ActivityPostModel)
class ActivityPostAdmin(admin.ModelAdmin):
    r"""ActivityPostAdmin

    ActivityPostAdmin is a admin.ModelAdmin.
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

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = ((None, {
        "fields": ["title", "status", ("publish_date", "expiry_date"), 'body'],
    }),
    )


@admin.register(NewsPostModel)
class NewsPostAdmin(admin.ModelAdmin):
    r"""NewsPostAdmin

    NewsPostAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'category', 'status', 'url', 'publish_date', 'expiry_date')
    list_editable = ('status', )
    ordering = ('-modified', )
    radio_fields = {"status": admin.HORIZONTAL}

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = ((None, {
        "fields": ['title', 'url',  'category', ('publish_date', 'expiry_date'), 'status'],
    }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
