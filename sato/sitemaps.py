#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sitemaps -- DESCRIPTION

"""
from django.contrib import sitemaps


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['news', 'activity', 'security', 'security/secportal',
                'security/knowledge', 'board', 'formats', 'about', 'about/hall',
                'about/solve', 'about/group', 'about/rule']

    def location(self, item):
        return '/' + item + '/'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sitemaps.py ends here
