#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from todo.models import TodoEntryModel


class TodoAdmin(admin.ModelAdmin):
    r"""TodoAdmin

    TodoAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'description', 'created', 'category', 'finished')
    # filter_horizontal = ('finished',)
    list_editable = ('finished', )
    list_filter = ('finished', )


admin.site.register(TodoEntryModel, admin.ModelAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
