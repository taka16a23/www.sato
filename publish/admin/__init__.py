#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin
from publish.admin.board import DocumentAdmin
from publish.admin.activity import ActivityPostAdmin, TagModelAdmin
from publish.admin.news import NewsPostAdmin, NewsCategoryAdmin
from publish.models import (
    TagModel, ActivityPostModel, DocumentModel, NewsPostModel, NewsCategoryModel)


__all__ = ['DocumentAdmin', 'ActivityPostAdmin', 'NewsPostAdmin', 'TagModelAdmin', ]


admin.site.register(TagModel, TagModelAdmin)
admin.site.register(ActivityPostModel, ActivityPostAdmin)
admin.site.register(DocumentModel, DocumentAdmin)
admin.site.register(NewsPostModel, NewsPostAdmin)
admin.site.register(NewsCategoryModel, NewsCategoryAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
