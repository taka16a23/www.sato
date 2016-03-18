#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py

"""
from django.contrib import admin
from django.shortcuts import redirect

from about.admin.contact import ContactReceiverAdmin, ContactedAdmin
from about.admin.qa import QAAdmin
from about.models import ContactReceiverModel, ContactedModel, QAModel


__all__ = ['QAAdmin', 'ContactReceiverAdmin', 'ContactedAdmin', ]


@admin.site.register_view('pathname', u'プロバイダー契約　ユーザーID: ts773544　パスワード: ts773544@qj8')
def provider_view(request, *args, **kwargs):
    r"""SUMMARY

    my_view(request, *args, **kwargs)

    @Arguments:
    - `request`:
    - `args`:
    - `kwargs`:

    @Return:

    @Error:
    """
    return redirect('http://www.so-net.ne.jp/mypage/')


admin.site.register(ContactReceiverModel, ContactReceiverAdmin)
admin.site.register(ContactedModel, ContactedAdmin)
admin.site.register(QAModel, QAAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
