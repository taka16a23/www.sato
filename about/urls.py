#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import patterns, url
from about.group import views

urlpatterns = patterns(
    '',
    # url(r'^$', views.index, name='index'),
    url(r'^group/', views.group, name='group')
)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
