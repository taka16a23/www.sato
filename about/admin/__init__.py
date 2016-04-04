#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin

from about.admin.contact import (ContactReceiverAdmin, ContactedAdmin,
                                 HallReceiverAdmin)
from about.admin.qa import QAAdmin
from about.models import (
    ContactReceiverModel, ContactedModel, QAModel, HallReceiverModel)


__all__ = ['QAAdmin', 'ContactReceiverAdmin',
           'ContactedAdmin', 'HallReceiverAdmin']


admin.site.register(ContactReceiverModel, ContactReceiverAdmin)
admin.site.register(HallReceiverModel, HallReceiverAdmin)
admin.site.register(ContactedModel, ContactedAdmin)
admin.site.register(QAModel, QAAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
