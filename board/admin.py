#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from board.models import DocumentModel


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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
