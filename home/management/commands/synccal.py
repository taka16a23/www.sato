#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""synccal -- DESCRIPTION

"""
from django.core.management import BaseCommand, CommandError
from home import controllers

from dateutil import parser as dateparser


class Command(BaseCommand):
    r"""Command

    Command is a BaseCommand.
    Responsibility:
    """
    help = 'Syncronize Google Calendars.'

    def add_arguments(self, parser):
        r"""SUMMARY

        add_arguments(parser)

        @Arguments:
        - `parser`:

        @Return:

        @Error:
        """
        parser.add_argument('-m', '--main',
                            dest='main',
                            action='store_true',
                            default=False,
                            help='Sync with main calendar.')
        parser.add_argument('-g', '--garbage',
                            dest='garbage',
                            action='store_true',
                            default=False,
                            help='Sync with garbage calendar.')
        parser.add_argument('-l', '--hall',
                            dest='hall',
                            action='store_true',
                            default=False,
                            help='Sync with hall calendar.')
        parser.add_argument('-c', '--counts',
                            dest='counts',
                            action='store',
                            default=250,
                            type=int,
                            # (yas-expand-link "argparse_other_options" t)
                            help='Sync event counts from start date.')
        parser.add_argument('-s', '--start',
                            dest='start',
                            action='store',
                            default='',
                            help='''Sync from start date.
                            2010/6/30 23:15:22
                            2010-06-30
                            20100630
                            Mon, 27 Oct 2008 21:24:07 +0900 (JST)
                            ''')
        # (yas-expand-link "argparse_add_argument" t)

    def handle(self, *args, **options):
        r"""SUMMARY

        @Arguments:
        - `*args`:
        - `**options`:

        @Return:

        handle()

        @Error:
        """
        if options['start']:
            start = dateparser.parse(options['start'])
        else:
            start = None
        # manage.py synccal
        if not (options['main'] or options['garbage'] or options['hall']):
            options['main'] = options['garbage'] = options['hall'] = True
        # ./manage.py synccal main
        if options['main']:
            controllers.sync_main_calendar(start=start, counts=options['counts'])
        # ./manage.py synccal garbage
        if options['garbage']:
            controllers.sync_garbage_calendar(start=start, counts=options['counts'])
        # ./manage.py synccal hall
        if options['hall']:
            controllers.sync_hall_calendar(start=start, counts=options['counts'])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# synccal.py ends here
