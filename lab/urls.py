#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url

from lab import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # (r'^$', 'lab.views.lab_view'),
    url('^server/', views.server_view),
    url('^weather/', views.weather_view),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
