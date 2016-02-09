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
    # url(r'^group/', groupview, name='group'),
    (r'^group/', 'about.group.views.groupview'),
    (r'^contact/thankyou/', 'about.contact.views.thankyou'),
    (r'^contact/', 'about.contact.views.contactform'),
    (r'^$', 'about.views.about_view'),
)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
