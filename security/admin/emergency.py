#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""emergency -- DESCRIPTION

"""
from django.contrib import admin
from security.models import EmergencyEntryModel


def make_unpublish(modeladmin, request, queryset):
    r"""SUMMARY

    unpublish_all(modeladmin, request, queryset)

    @Arguments:
    - `modeladmin`:
    - `request`:
    - `queryset`:

    @Return:

    @Error:
    """
    queryset.update(status=2)


make_unpublish.short_description = u'非公開にする'


class EmergencyEntryAdmin(admin.ModelAdmin):
    r"""EmergencyEntryAdmin

    EmergencyEntryAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'status', 'publish_date', 'expiry_date', 'description')
    list_editable = ('status', )
    ordering = ('-modified', )
    exclude = ('description', )
    radio_fields = {"status": admin.HORIZONTAL}
    actions = [make_unpublish, 'delete_selected']

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = ((None, {
        "fields": ["title", "status", ("publish_date", "expiry_date"), 'body'],
    }),
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# emergency.py ends here
