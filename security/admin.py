#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from security.models import SecKnowledgeModel, EmergencyEntryModel
from adminsortable2.admin import SortableAdminMixin

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

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = ((None, {
        "fields": ["title", "status", ("publish_date", "expiry_date"), 'body'],
    }),
    )


@admin.register(SecKnowledgeModel)
class SecKnowledgeAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""SecKnowledgeAdmin

    SecKnowledgeAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'short_description', 'url', 'thumbnail', 'publish')
    list_editable = ('publish', )
    exclude = ['sortid', 'short_description', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
