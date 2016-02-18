#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from emergency.models import EmergencyEntryModel
from sato.settings import STATIC_URL


# admin.site.disable_action('delete_selected')

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

@admin.register(EmergencyEntryModel)
class EmergencyEntryAdmin(admin.ModelAdmin):
    r"""EmergencyEntryAdmin

    EmergencyEntryAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'status', 'publish_date', 'expiry_date', 'body')
    list_editable = ('status', )
    ordering = ('-modified', )
    radio_fields = {"status": admin.HORIZONTAL}
    actions = [make_unpublish, 'delete_selected']

    class Media:
        js = (STATIC_URL + 'tiny_mce/tiny_mce.js',
              STATIC_URL + 'tiny_mce/simple_tiny_mce.js',)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
