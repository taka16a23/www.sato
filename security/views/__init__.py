#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from security.views.knowledge import knowledge_view
from security.views.portal import secportal_view
from security.views.index import security_view

__all__ = ['knowledge_view', 'secportal_view', 'security_view', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
