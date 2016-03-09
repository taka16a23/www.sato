#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""contact -- DESCRIPTION

"""
from django.contrib import admin
from about.models import ContactPostModel, ContactReceiverModel, ContactedModel


@admin.register(ContactPostModel)
class ContactAdmin(admin.ModelAdmin):
    r"""ContactAdmin

    ContactAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('name', 'created', 'email', 'body',  'finished')
    list_editable = ('finished', )
    # radio_fields = {"finished": admin.HORIZONTAL}


@admin.register(ContactReceiverModel)
class ContactReceiverAdmin(admin.ModelAdmin):
    r"""ContactReceiverAdmin

    ContactReceiverAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('name', 'email', 'active', )
    list_editable = ('active', )
    exclude = ('created', 'modified', )
    # radio_fields = {"active": admin.HORIZONTAL}


@admin.register(ContactedModel)
class ContactedAdmin(admin.ModelAdmin):
    r"""ContactedAdmin

    ContactedAdmin is a admin.ModelAdmin.
    Responsibility:
    """
    list_display = ('id', 'name', 'email', 'status')
    list_editable = ('status', )
    exclude = ('created', 'modified', )
    readonly_fields = ('id', )
    # radio_fields = {"status": admin.HORIZONTAL}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# contact.py ends here
