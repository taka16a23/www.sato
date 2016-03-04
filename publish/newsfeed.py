#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""newsfeed -- DESCRIPTION

"""
from django.contrib.syndication.views import Feed
from publish.models import NewsPostModel


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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# newsfeed.py ends here
