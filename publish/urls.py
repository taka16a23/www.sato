#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""urls -- DESCRIPTION

"""
from django.conf.urls import url, patterns, include
from django.contrib.syndication.views import Feed

from publish.models import NewsPostModel
from publish.views import news_view


class NewsFeed(Feed):
    r"""NewsFeed

    NewsFeed is a Feed.
    Responsibility:
    """
    title = "Test"
    description = "Test description"
    link = "/news/feed/"

    def items(self, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        return NewsPostModel.objects.published().order_by('-publish_date')[:10]

    def item_title(self, item):
        r"""SUMMARY

        item_title(item)

        @Arguments:
        - `item`:

        @Return:

        @Error:
        """
        return item.title

    def item_description(self, item):
        r"""SUMMARY

        item_description(item)

        @Arguments:
        - `item`:

        @Return:

        @Error:
        """
        return item.as_category_name()

    def item_link(self, item):
        r"""SUMMARY

        item_link(item)

        @Arguments:
        - `item`:

        @Return:

        @Error:
        """
        return item.url


urlpatterns = [
    url('^feed/', NewsFeed()),
    url('^$', news_view),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
