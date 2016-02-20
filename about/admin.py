#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from sato.settings import STATIC_URL
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
    list_display = ('question', 'answer', 'status', )
    list_editable = ('status', )
    radio_fields = {'status': admin.HORIZONTAL,}

    class Media:
        js = (STATIC_URL + 'tiny_mce/tiny_mce.js',
              STATIC_URL + 'tiny_mce/simple_tiny_mce.js',)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
