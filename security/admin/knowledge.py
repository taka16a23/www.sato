#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""knowledge -- DESCRIPTION

"""
from django.contrib import admin
from security.models import SecKnowledgeModel
from adminsortable2.admin import SortableAdminMixin


@admin.register(SecKnowledgeModel)
class SecKnowledgeAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""SecKnowledgeAdmin

    SecKnowledgeAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('title', 'short_description', 'thumbnail', 'publish')
    list_editable = ('publish', )
    exclude = ['sortid', 'short_description', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# knowledge.py ends here
