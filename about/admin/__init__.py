#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin

from about.admin.contact import ContactReceiverAdmin, ContactedAdmin
from about.admin.qa import QAAdmin
from about.models import ContactReceiverModel, ContactedModel, QAModel


__all__ = ['QAAdmin', 'ContactReceiverAdmin', 'ContactedAdmin', ]

admin.site.register(ContactReceiverModel, ContactReceiverAdmin)
admin.site.register(ContactedModel, ContactedAdmin)
admin.site.register(QAModel, QAAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
