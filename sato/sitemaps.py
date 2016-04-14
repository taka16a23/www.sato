#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sitemaps -- DESCRIPTION

"""
from django.contrib import sitemaps
from publish.models import ActivityPostModel


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['news', 'activity', 'security', 'security/secportal',
                'security/knowledge', 'board', 'formats', 'about', 'about/hall',
                'about/solve', 'about/group', 'about/rule']

    def location(self, item):
        return '/' + item + '/'


class ActivityPostSitemap(sitemaps.Sitemap):
    r"""ActivityPostSitemap

    ActivityPostSitemap is a sitemaps.Sitemap.
    Responsibility:
    """
    changefreq = "monthly"
    priority = 0.5

    def items(self, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        return ActivityPostModel.objects.published()

    def lastmod(self, obj):
        r"""SUMMARY

        lastmod(obj)

        @Arguments:
        - `obj`:

        @Return:

        @Error:
        """
        return obj.modified

    def location(self, item):
        r"""SUMMARY

        location(item)

        @Arguments:
        - `item`:

        @Return:

        @Error:
        """
        return '/activity/' + str(item.id)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sitemaps.py ends here
