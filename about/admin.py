#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from about.models import ContactPostModel
from about.models import QAModel

from adminsortable2.admin import SortableAdminMixin


@admin.register(ContactPostModel)
class ContactAdmin(admin.ModelAdmin):
    r"""ContactAdmin

    ContactAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('name', 'created', 'email', 'body',  'finished')
    list_editable = ('finished', )
    # radio_fields = {"finished": admin.HORIZONTAL}


@admin.register(QAModel)
class QAAdmin(SortableAdminMixin, admin.ModelAdmin):
    r"""QAAdmin

    QAAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('question', 'description', 'status', )
    list_editable = ('status', )
    exclude = ('sortid', 'description', )
    radio_fields = {'status': admin.HORIZONTAL,}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
