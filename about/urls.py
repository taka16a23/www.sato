#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # url(r'^$', views.index, name='index'),
    (r'^group/', 'about.views.group_view'),
    (r'^solve/', 'about.views.solve_view'),
    (r'^thankyou/', 'about.views.thankyou'),
    (r'^$', 'about.views.about_view'),
)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
