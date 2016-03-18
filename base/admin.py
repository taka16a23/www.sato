#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.admin import UserAdmin, User, Group, GroupAdmin


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


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
