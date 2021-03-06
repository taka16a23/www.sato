#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.admin import UserAdmin, User, Group, GroupAdmin
from base.views import month_schedules_view # for register


@admin.site.register_view('xxx', u'プロバイダー　ID: ts773544@qj8　パスワード: pgy43crg')
def provider_mail(request, *args, **kwargs):
    """SUMMARY

    provider_mail(request, *args, **kwargs)

    @Arguments:
    - `request`:
    - `args`:
    - `kwargs`:

    @Return:

    @Error:
    """
    return redirect('https://www.so-net.ne.jp/mypage/')


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# admin.py ends here
