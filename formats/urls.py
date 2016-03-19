#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url, patterns, include
from formats.views import formats_view


urlpatterns = [
    url('^$', formats_view),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
