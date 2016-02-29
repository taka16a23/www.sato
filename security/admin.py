#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from security.models import SecKnowledgeModel, EmergencyEntryModel

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
    list_display = ('title', 'status', 'publish_date', 'expiry_date', 'description')
    list_editable = ('status', )
    ordering = ('-modified', )
    exclude = ('description', )
    radio_fields = {"status": admin.HORIZONTAL}
    actions = [make_unpublish, 'delete_selected']


@admin.register(SecKnowledgeModel)
class SecKnowledgeAdmin(admin.ModelAdmin):
    r"""SecKnowledgeAdmin

    SecKnowledgeAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'description', 'url', 'thumbnail', 'sortid', 'publish')
    ordering = ('sortid', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
