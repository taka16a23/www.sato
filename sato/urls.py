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
from django.views.static import serve as static_serve
from django.conf.urls.static import static

from sato import settings
# from sato.admin import admin_site
from home.views import home_view
from activity.views import activity_view
from board.views import board_view
from formats.views import formats_view


urlpatterns = [
    url(r'^$', home_view),
    url(r'^news/', include('news.urls')),
    url(r'^security/', include('security.urls')),
    url(r'^activity/', activity_view),
    url(r'^board/', board_view),
    url(r'^formats/', formats_view),
    url(r'^about/', include('about.urls')),
    url(r'^admin/', admin.site.urls),
    # url(r'^admin/', include(admin_site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^lab/', include('lab.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [url(r'^captcha/', include('captcha.urls'))]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_serve,
            {'document_root': settings.MEDIA_ROOT}), ]

admin.site.site_title = u'里自治会'
admin.site.site_header = u'里自治会 ホームページ'
admin.site.index_title = u'コントロールパネル'



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# urls.py ends here
