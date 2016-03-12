#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""functions -- DESCRIPTION

"""
from BeautifulSoup import BeautifulSoup


def get_plaintext(text):
    r"""SUMMARY

    get_plaintext(text)

    @Arguments:
    - `text`:

    @Return:

    @Error:
    """
    soup = BeautifulSoup(unicode(text))
    [s.extract() for s in soup('script')]
    return u''.join([s.replace('&nbsp;', '') for s in soup.findAll(text=True)])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# functions.py ends here
