#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url, patterns, include
from formats.views import form_hallbooking_view, formats_view


urlpatterns = [
    url('^form/hallbooking', form_hallbooking_view),
    url('^$', formats_view),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
