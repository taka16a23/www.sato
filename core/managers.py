#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""managers -- DESCRIPTION

"""
from django.db.models import Manager, Q
from django.db.models.query import QuerySet

import datetime


class ManagerAbstract(Manager):
    r"""ManagerAbstract

    ManagerAbstract is a models.Manager.
    Responsibility:
    """
    def __getattr__(self, name):
        return getattr(self.get_query_set(), name)


class DisplayableQuerySet(QuerySet):
    r"""DisplayableQuerySet

    DisplayableQuerySet is a QuerySet.
    Responsibility:
    """
    def published(self, ):
        r"""SUMMARY

        published()

        @Return:

        @Error:
        """
        from core.models import DISPLAY_STATUS_PUBLISHED
        now = datetime.datetime.now()
        return self.filter(
            Q(publish_date__lte=now)|Q(publish_date__isnull=True),
            Q(expiry_date__gte=now)|Q(expiry_date__isnull=True),
            Q(status=DISPLAY_STATUS_PUBLISHED))

    def range_by_publish_date(self, start, end):
        r"""SUMMARY

        range_by_publish_date(start, end)

        @Arguments:
        - `start`:
        - `end`:

        @Return:

        @Error:
        """
        return self.filter(
            Q(publish_date__gte=start)|Q(publish_date__isnull=True),
            Q(publish_date__lte=end)|Q(publish_date__isnull=True))

    def by_fiscal_year(self, year):
        r"""SUMMARY

        by_fiscal_year(year)

        @Arguments:
        - `year`:

        @Return:

        @Error:
        """
        return self.filter(Q(fiscal_year=year))

    def uniq_fiscal_years(self, ):
        r"""SUMMARY

        uniq_fiscal_years()

        @Return:

        @Error:
        """
        years = [d['fiscal_year'] for d in self.values('fiscal_year').distinct()]
        years.sort()
        return years


class DisplayableManager(ManagerAbstract):
    r"""DisplayableManager

    DisplayableManager is a ManagerAbstract.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return DisplayableQuerySet(self.model)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# managers.py ends here
