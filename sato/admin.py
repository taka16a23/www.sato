#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""admin -- DESCRIPTION

"""
from django.contrib.admin import AdminSite

class SatoAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    # site_title = u'里自治会'

    # Text to put in each page's <h1>.
    site_header = u'里自治会ホームページ コントロールパネル'

    # Text to put at the top of the admin index page.
    # index_title = u'里自治会ホームページ コントロールパネル'

admin_site = SatoAdminSite()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
