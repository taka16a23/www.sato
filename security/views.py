#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from lib.utils import get_context
from security.models import SecKnowledgeModel

import datetime
from collections import namedtuple
import requests
from lxml import html
import urlparse


def security_view(request):
    r"""SUMMARY

    security_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    return render_to_response(
        'security/index.html', context, context_instance=RequestContext(request))


# for security portal
WeatherWarnings = namedtuple(
    'WeatherWarnings',
    (
        # Em = Emergency
        'Em_Snow_storm', # 暴風雪特別警報
        'Em_Landslide_disaster', # 土砂災害特別警報
        'Em_Flood_damage', # 浸水害特別警報
        'Em_Storm', # 暴風特別警報
        'Em_Heavy_snow', # 大雪特別警報
        # Wa = Warning
        'Wa_Snow_storm', # 暴風雪警報
        'Wa_Landslide_disaster', # 土砂災害警報
        'Wa_Flood_damage', # 浸水害警報
        'Wa_Flood', # 洪水警報
        'Wa_Storm', # 暴風警報
        'Wa_Heavy_snow', # 大雪警報
        # Ad = Advisory
        'Ad_Heavy_rain', # 大雨注意報
        'Ad_Heavy_snow', # 大雪注意報
        'Ad_Gale_and_snow', # 風雪注意報
        'Ad_Thunderstorm', # 雷注意報
        'Ad_Gale', #強風注意報
        'Ad_Snow_melting', # 融雪注意報
        'Ad_Flood', # 洪水注意報
        'Ad_Dense_fog', # 濃霧注意報
        'Ad_Dry_air', # 乾燥注意報
        'Ad_Avalanche', # なだれ注意報
        'Ad_Low_temperature', # 低温注意報
        'Ad_Frost', # 霜注意報
        'Ad_Ice_accretion', # 着氷注意報
        'Ad_Snow_accretion', # 着雪注意報
    ))


def get_weather_warnings(soup):
    r"""SUMMARY

    get_weather_warnings()

    @Return:

    @Error:
    """
    th_list = soup.xpath('//*[@id="mainContentsContainer"]/table[1]/tr/th')
    tr = None
    for th in th_list:
        if u'大津市南部' == th.text:
            tr = th.getparent()
            break
    if tr is None:
        return None
    td_list = tr.xpath('td')
    return WeatherWarnings(*[td.text for td in td_list])


def get_warnings_last_date(soup):
    r"""SUMMARY

    get_warnings_last_date(soup)

    @Arguments:
    - `soup`:

    @Return:

    @Error:
    """
    return soup.xpath(
        '//*[@id="mainTitleContainer"]/font')[0].text.replace(u'　', '')


def floor(src, range):
    """
    floor(21, 5) #21分を5分で切り捨て
    >>> 20
    """
    return (int)(src / range) * range

def ceil(src, range):
    """
    floor(21, 5) #21分を5分で切り上げ
    >>> 25
    """
    return ((int)(src / range) + 1 ) * range


BASEURL = 'http://shiga-bousai.jp'

def get_graph(suburl, xpath):
    r"""SUMMARY

    get_graph(suburl, xpath)

    @Arguments:
    - `suburl`:
    - `xpath`:

    @Return:

    @Error:
    """
    page_url = urlparse.urljoin(BASEURL, suburl)
    res = requests.get(page_url)
    if not res.ok:
        return ''
    soup = html.fromstring(res.text)
    return urlparse.urljoin(BASEURL, soup.xpath(xpath)[0].attrib.get('src', ''))


def url_rain_graph():
    r"""SUMMARY

    url_rain_graph()

    @Return:

    @Error:
    """
    return get_graph(
        'rain/rain_graph03.php?id1=6&id2=4&id3=1&id4=13&sid=21302',
        '//*[@id="mainContentsLeftColumn"]/img')


def url_river_graph():
    r"""SUMMARY

    url_river_graph()

    @Return:

    @Error:
    """
    return get_graph(
        'wl/wl_graph02.php?interval=60&id1=7&id2=4&id3=1&id4=13&sid=12056&page=2',
        '//*[@id="mainContentsLeftColumn"]/a[1]/img')


def secportal_view(request):
    r"""SUMMARY

    secportal_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context(emergency=True)
    now = datetime.datetime.now()
    # 取得先より時間がすすんでいると画像が取得できない
    # 数十秒過去に調整
    # TODO: (Atami) [2016/02/14]
    # ntpdate で時間を定期的に調整
    fixed = now - datetime.timedelta(seconds=30)
    context['camdate'] = datetime.datetime(
        fixed.year, fixed.month, fixed.day, fixed.hour, floor(fixed.minute, 5))

    # get warnings
    res = requests.get('http://shiga-bousai.jp/announce/weather.php')
    try:
        if not res.ok:
            context['warnings'] = None
        else:
            soup = html.fromstring(res.text)
            context['warnings_date'] = get_warnings_last_date(soup)
            context['warnings'] = get_weather_warnings(soup)
    except StandardError as err:
        print(err)
    context['rainGraph'] = url_rain_graph()
    context['riverGraph'] = url_river_graph()
    return render_to_response(
        'secportal/index.html', context,
        context_instance=RequestContext(request))

def knowledge_view(request):
    r"""SUMMARY

    knowledge_view(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = get_context()
    context['knowledges'] = SecKnowledgeModel.objects.filter(publish=True).order_by('sortid')
    return render_to_response(
        'knowledge/index.html',
        context,
        context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# views.py ends here
