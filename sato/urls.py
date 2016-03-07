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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as static_serve

from sato import settings
# from sato.admin import admin_site
from home.views import home_view
from publish.views import activity_view, activity_list_view
from publish.views import board_view
from publish.views import news_view
from publish.newsfeed import NewsFeed
from django.views.generic.base import RedirectView

from filebrowser.sites import site

urlpatterns = [
    url(r'^$', home_view),
    url(r'^news/feed/', NewsFeed()),
    url(r'^news/', news_view),
    url(r'^security/', include('security.urls')),
    url(r'^activity/(?P<postid>\d+)', activity_view, name='activityid'),
    url(r'^activity/', activity_list_view),
    url(r'^board/', board_view),
    url(r'^formats/', include('formats.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^lab/', include('lab.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico'))
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
