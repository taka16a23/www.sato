#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""activity -- DESCRIPTION

"""
from django.contrib import admin
from publish.models import ActivityPostModel, TagModel


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    r"""TagModelAdmin

    TagModelAdmin is a admin.ModelAdmin.
    Responsibility:
    """

@admin.register(ActivityPostModel)
class ActivityPostAdmin(admin.ModelAdmin):
    r"""ActivityPostAdmin

    ActivityPostAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    model = ActivityPostModel

    filter_horizontal = ['tags', ]

    list_display = ('title', 'publish_date', 'expiry_date',
                    'description', '_tags', 'status', )
    list_display_links = ("title", )
    list_editable = ('status', )
    ordering = ('-modified', )
    exclude = ('description', )
    radio_fields = {"status": admin.HORIZONTAL}
    date_hierarchy = 'publish_date'
    list_filter = ('status', 'publish_date', 'expiry_date', 'tags')

    class Media:
        css = {'all': ('css/admin_sato.css', ),}

    fieldsets = ((None, {
        "fields": ["title", "status", ("publish_date", "expiry_date"),
                   'body', 'tags'],
    }),
    )

    def _tags(self, row):
        return ','.join([x.name for x in row.tags.all()])

    def save_related(self, request, form, formsets, change):
        super(ActivityPostAdmin, self).save_related(request, form, formsets, change)
        # add tag of 年度
        instance = form.instance
        fiscalyear = instance.publish_date.year
        if instance.publish_date.month in (1, 2, 3):
            fiscalyear -= 1
        fiscalyearname = unicode(fiscalyear) + u'年度'
        tag, created = TagModel.objects.get_or_create(
            name=fiscalyearname, defaults={'name': fiscalyearname,})
        print(type(tag))
        if not tag in list(instance.tags.all()):
            instance.tags.add(tag)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# activity.py ends here
