#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""admin -- DESCRIPTION

"""
from django.contrib.admin import AdminSite
from adminplus.sites import AdminSitePlus


class SatoAdminSite(AdminSitePlus):
    # Text to put at the end of each page's <title>.
    # site_title = u'里自治会'

    # Text to put in each page's <h1>.
    # site_header = u'里自治会ホームページ コントロールパネル'
    # site_title = u'里自治会'
    site_header = u'里自治会 ホームページ'
    index_title = u'コントロールパネル'
    # index_template = 'base/admin/index.html'
    # Text to put at the top of the admin index page.
    # index_title = u'里自治会ホームページ コントロールパネル'

admin_site = SatoAdminSite()

# admin_site.index_template = 'base/admin/index.html'
# admin_site.site_title = u'里自治会'
# admin_site.site_header = u'里自治会 ホームページ'
# admin_site.index_title = u'コントロールパネル'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
