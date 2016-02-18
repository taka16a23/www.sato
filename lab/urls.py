#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import patterns, url
# from about.group.views import groupview
# from about.contact.views import contactform


urlpatterns = patterns(
    '',
    # url(r'^$', views.index, name='index'),
    # (r'^$', 'lab.views.lab_view'),
    url('^server/', 'lab.views.server_view'),
)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
