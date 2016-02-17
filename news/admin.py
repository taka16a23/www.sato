#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import PostModel


@admin.register(PostModel)
class NewsPostAdmin(admin.ModelAdmin):
    r"""NewsPostAdmin

    NewsPostAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'category', 'status', 'url', 'publish_date', 'expiry_date')
    list_editable = ('status', )
    ordering = ('-modified', )
    radio_fields = {"status": admin.HORIZONTAL}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
