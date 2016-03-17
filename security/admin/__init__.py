#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin

from security.admin.emergency import EmergencyEntryAdmin, make_unpublish
from security.admin.knowledge import SecKnowledgeAdmin
from security.models import SecKnowledgeModel, EmergencyEntryModel


__all__ = ['EmergencyEntryAdmin', 'SecKnowledgeAdmin', 'make_unpublish', ]


admin.site.register(SecKnowledgeModel, SecKnowledgeAdmin)
admin.site.register(EmergencyEntryModel, EmergencyEntryAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
