# -*- coding: utf-8 -*-

from django.contrib import admin
from emergency.models import Emergency


# Register your models here.
admin.site.disable_action('delete_selected')

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
    queryset.update(publish=False)

make_unpublish.short_description = u'非公開にする'


class EmergencyAdmin(admin.ModelAdmin):
    r"""EmergencyAdmin

    EmergencyAdmin is a admin.Model.
    Responsibility:
    """
    list_display = ('title', 'publish', 'mtime', 'description')
    list_editable = ('publish',)

    actions = [make_unpublish, 'delete_selected']


admin.site.register(Emergency, EmergencyAdmin)
