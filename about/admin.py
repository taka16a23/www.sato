#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from about.models import ContactPostModel
from about.models import QAModel


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
class QAAdmin(admin.ModelAdmin):
    r"""QAAdmin

    QAAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('question', 'description', 'status', )
    list_editable = ('status', )
    exclude = ('description', )
    radio_fields = {'status': admin.HORIZONTAL,}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
