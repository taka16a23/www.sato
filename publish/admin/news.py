#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news -- DESCRIPTION

"""
from django.contrib import admin
from publish.models import NewsPostModel


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
# news.py ends here
