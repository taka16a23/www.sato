#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    (r'^secportal/', 'security.views.secportal_view'),
    (r'^knowledge/', 'knowledge.views.knowledge_view'),
    (r'^$', 'security.views.security_view'),
)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
