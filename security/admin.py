#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from sato.settings import STATIC_URL
from security.models import SecKnowledgeModel

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
