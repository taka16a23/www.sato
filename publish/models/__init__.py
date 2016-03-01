#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from publish.models.activity import ActivityPostModel
from publish.models.board import DocumentModel, validate_file_pdf
from publish.models.news import NewsPostModel, NewsCategoryModel


__all__ = ['ActivityPostModel', 'DocumentModel',
           'validate_file_pdf', 'NewsPostModel', 'NewsCategoryModel', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
