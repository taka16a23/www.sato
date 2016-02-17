#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""sato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.syndication.views import Feed

from sato import settings
# from sato.admin import admin_site

import datetime

urlpatterns = [
    url(r'^$', 'home.views.home'),
    url(r'^news/', include('news.urls')),
    url(r'^security/', include('security.urls')),
    url(r'^activity/', 'activity.views.view'),
    url(r'^board/', 'board.views.view'),
    url(r'^formats/', 'formats.views.formats'),
    url(r'^about/', include('about.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^admin/', include(admin_site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^lab/', include('lab.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', url(r'^captcha/', include('captcha.urls')))

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

admin.site.site_header = u'里自治会 ホームページ'
admin.site.index_title = u'コントロールパネル'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
