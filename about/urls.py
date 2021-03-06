#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url

from about import views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^group/', views.group_view),
    url(r'^solve/', views.solve_view),
    url(r'^thankyou/', views.thankyou),
    url(r'^rule/', views.rule),
    url(r'^greeding/', views.greeding),
    url(r'^hall/', views.form_hall_view),
    url(r'^children/', views.children),
    url(r'^$', views.about_view),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
