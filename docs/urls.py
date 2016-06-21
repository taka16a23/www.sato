#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url

from docs import views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^easy_add_board/', views.easy_add_board_view),
    url(r'^publish_calendar/', views.publish_calendar_view),
    url(r'^easy_add_activity/', views.easy_add_activity_view),
    # url(r'^solve/', views.solve_view),
    # url(r'^thankyou/', views.thankyou),
    # url(r'^rule/', views.rule),
    # url(r'^greeding/', views.greeding),
    # url(r'^hall/', views.form_hall_view),
    url(r'^$', views.top_view),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
