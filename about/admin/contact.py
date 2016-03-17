#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""contact -- DESCRIPTION

"""
from django.contrib import admin


class ContactReceiverAdmin(admin.ModelAdmin):
    r"""ContactReceiverAdmin

    ContactReceiverAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('name', 'email', 'active', )
    list_editable = ('active', )
    exclude = ('created', 'modified', )
    # radio_fields = {"active": admin.HORIZONTAL}


class ContactedAdmin(admin.ModelAdmin):
    r"""ContactedAdmin

    ContactedAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('_get_id', 'name', 'created', 'email', 'status')
    list_display_links = ('name', )
    list_editable = ('status', )
    exclude = ('modified', )
    readonly_fields = ('id', )
    # radio_fields = {"status": admin.HORIZONTAL}
    list_filter = ('status', 'name', )

    def _get_id(self, obj):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return obj.id

    _get_id.short_description = u'受付番号'

    def has_add_permission(self, request):
        return False



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# contact.py ends here
