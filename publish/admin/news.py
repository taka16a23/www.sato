#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""news -- DESCRIPTION

"""
from django.contrib import admin
from publish.models import NewsPostModel, NewsCategoryModel
from adminsortable2.admin import SortableAdminMixin



PRIMARY_CATEGORIES = [u'お知らせ', u'回覧']


@admin.register(NewsCategoryModel)
class NewsCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""NewsCategoryAdmin

    NewsCategoryAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('name', 'fgcolor', 'bgcolor', )
    list_editable = ('fgcolor', 'bgcolor', )
    exclude = ['sortid', ]

    def get_actions(self, request):
        actions = super(NewsCategoryAdmin, self).get_actions(request)
        if actions.has_key('delete_selected'):
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        r"""SUMMARY

        has_delete_permission(request, obj=None)

        @Arguments:
        - `request`:
        - `obj`:

        @Return:

        @Error:
        """
        if obj is not None and obj.name in PRIMARY_CATEGORIES:
            return False
        return super(NewsCategoryAdmin, self).has_delete_permission(request, obj=None)


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
