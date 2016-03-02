#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""board -- DESCRIPTION

"""
from django.contrib import admin
from publish.models import DocumentModel


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

    fieldsets = ((None, {
        'fields': ['title', ('publish_date', 'expiry_date'), 'file', 'status'],
    }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# board.py ends here
