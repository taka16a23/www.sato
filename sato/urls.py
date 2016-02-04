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
import home.views


from django.contrib.syndication.views import Feed
from informations.models import Information, INFO_CATEGORIES
import datetime


class InformationFeed(Feed):
    r"""InformationFeed

    InformationFeed is a Feed.
    Responsibility:
    """
    title = "Test"
    description = "Test description"
    link = "/informations/feed/"

    def items(self, ):
        r"""SUMMARY

        items()

        @Return:

        @Error:
        """
        now = datetime.datetime.now()
        return Information.objects.filter(publish=True).filter(pub_date__lte=now).order_by('-pub_date')[:10]

    def item_title(self, item):
        r"""SUMMARY

        item_title(item)

        @Arguments:
        - `item`:

        @Return:

        @Error:
        """
        return item.title

    def item_description(self, item):
        r"""SUMMARY

        item_description(item)

        @Arguments:
        - `item`:

        @Return:

        @Error:
        """
        return {x: name for x, name in INFO_CATEGORIES}.get(item.category, u'')

    def item_link(self, item):
        r"""SUMMARY

        item_link(item)

        @Arguments:
        - `item`:

        @Return:

        @Error:
        """
        return item.url


urlpatterns = [
    url(r'^$', home.views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^informations/feed/$', InformationFeed()),
    url(r'^about/', include('about.urls')),
]

urlpatterns += staticfiles_urlpatterns()
