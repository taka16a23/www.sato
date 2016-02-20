#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url, include

from security import views

urlpatterns = [
    url(r'^secportal/', views.secportal_view),
    url(r'^knowledge/', views.knowledge_view),
    url(r'^$', views.security_view),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
