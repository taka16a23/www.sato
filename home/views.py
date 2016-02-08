# -*- coding: utf-8 -*-

from collections import namedtuple
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from informations.models import INFO_CATEGORIES, Information
from emergency.models import Emergency
from django.db.models import Q
from django.shortcuts import render_to_response
# from datetime import datetime, timedelta
from calendar import (MONDAY, TUESDAY, WEDNESDAY, THURSDAY,
                      FRIDAY, SATURDAY, SUNDAY)

import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

CALID_MAIN = 'satotanakami@gmail.com'
CALID_GARBAGE = 'c9uc1q8uiftrf0agsvvbpo6dvc@group.calendar.google.com'
CALID_HALL = '6m5ne5kcfmkek4t0ba37o95olo@group.calendar.google.com'

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

Namespace = namedtuple(
    'Namespace', ('auth_host_name', 'auth_host_port', 'logging_level',
                  'noauth_local_webserver'))


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        flags = Namespace(auth_host_name='localhost', auth_host_port=[8080, 8090],
                          logging_level='ERROR', noauth_local_webserver=False)
        # if flags:
        credentials = tools.run_flow(flow, store, flags)
        # else: # Needed only for compatibility with Python 2.6
            # credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def list_events(calendar_id, start, end, max_results=10):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    time_min = start.strftime('%Y-%m-%dT00:00:00.000000Z')
    time_max = end.strftime('%Y-%m-%dT23:59:59.999999Z')
    eventsResult = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min, timeMax=time_max, maxResults=max_results, singleEvents=True,
        orderBy='startTime').execute()
    return eventsResult.get('items', [])


Event = namedtuple('Event', ('colorId', 'created', 'url', 'id', 'kind',
                             'status', 'title', 'starttime'))
GarbageEvent = namedtuple('GarbageEvent', ('event', 'image'))


GARBAGE_IMGS = {u'紙ごみ': 'paper.jpg',
                u'燃やせるごみ': 'combustibles.jpg',
                u'透明びん、茶色びん': 'bottles.jpg',
                u'プラ容器包装': 'plastics.jpg',
                u'ペットボトル': 'PET.jpg',
                u'燃やせないごみ': 'incombustibles.jpg',
                u'かん': 'cans.jpg',
}

def list_garbage_events(start, end, max_results=10):
    r"""SUMMARY

    list_garbage_events(start, end, max_results=10)

    @Arguments:
    - `start`:
    - `end`:
    - `max_results`:

    @Return:

    @Error:
    """
    for ev in list_events(CALID_GARBAGE, start, end, max_results=max_results):
        starttime = ev.get('start', {}).get('dateTime', None)
        if starttime:
            starttime = starttime.split('T')[1].split('+')[0][:-3]
        image = GARBAGE_IMGS.get(ev.get('summary', ''), None)
        print(image)
        yield GarbageEvent(
            Event(colorId=ev.get('colorId', ''),
                  created=ev.get('created', ''),
                  url=ev.get('htmlLink', ''),
                  id=ev.get('id', ''),
                  kind=ev.get('kind', ''),
                  status=ev.get('status', ''),
                  title=ev.get('summary', ''),
                  starttime=starttime,), image=image)


def list_main_events(start, end, max_results=10):
    r"""SUMMARY

    list_main_events(start, end, max_results=10)

    @Arguments:
    - `start`:
    - `end`:
    - `max_results`:

    @Return:

    @Error:
    """
    for ev in list_events(CALID_MAIN, start, end, max_results=max_results):
        starttime = ev.get('start', {}).get('dateTime', None)
        if starttime:
            starttime = starttime.split('T')[1].split('+')[0][:-3]
        yield Event(colorId=ev.get('colorId', ''),
                  created=ev.get('created', ''),
                  url=ev.get('htmlLink', ''),
                  id=ev.get('id', ''),
                  kind=ev.get('kind', ''),
                  status=ev.get('status', ''),
                  title=ev.get('summary', ''),
                  starttime=starttime)


def list_hall_events(start, end, max_results=10):
    r"""SUMMARY

    list_hall_events(start, end, max_results=10)

    @Arguments:
    - `start`:
    - `end`:
    - `max_results`:

    @Return:

    @Error:
    """
    for ev in list_events(CALID_HALL, start, end, max_results=max_results):
        starttime = ev.get('start', {}).get('dateTime', None)
        if starttime:
            starttime = starttime.split('T')[1].split('+')[0][:-3]
        yield Event(colorId=ev.get('colorId', ''),
                  created=ev.get('created', ''),
                  url=ev.get('htmlLink', ''),
                  id=ev.get('id', ''),
                  kind=ev.get('kind', ''),
                  status=ev.get('status', ''),
                  title=ev.get('summary', ''),
                  starttime=starttime)


WEEKDAY_JDIC = {MONDAY: u'月',
                TUESDAY: u'火',
                WEDNESDAY: u'水',
                THURSDAY: u'木',
                FRIDAY: u'金',
                SATURDAY: u'土',
                SUNDAY: u'日'}

# Create your views here.
class Info(object):
    r"""Info

    Info is a object.
    Responsibility:
    """
    categories = {x: name for x, name in INFO_CATEGORIES} # tuple to dict

    def __init__(self, title, category, ctime, url):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.title = title
        self._category = category
        self._ctime = ctime
        self.url = url

    @property
    def category(self, ):
        r"""SUMMARY

        category()

        @Return:

        @Error:
        """
        return self.categories.get(self._category)

    @property
    def category_class(self, ):
        r"""SUMMARY

        category_class()

        @Return:

        @Error:
        """
        return {1: 'categoryImportant',
                2: 'categoryInfo',
                3: 'categorySecurity',
                4: 'categoryReport',
                5: 'categoryEvent',
                6: 'categoryWanted',
                7: 'categoryUpdate',
        }.get(self._category)

    @property
    def date(self, ):
        r"""SUMMARY

        date()

        @Return:

        @Error:
        """
        return self._ctime.strftime('%Y/%m/%d')


PAST_COUNTS = 7
MIN_INFO_COUNTS = 8

class Day(object):
    r"""Day

    Day is a object.
    Responsibility:
    """
    def __init__(self, date):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._date = date

    @property
    def year(self, ):
        r"""SUMMARY

        year()

        @Return:

        @Error:
        """
        return self._date.year

    @property
    def month(self, ):
        r"""SUMMARY

        month()

        @Return:

        @Error:
        """
        return self._date.month

    @property
    def day(self, ):
        r"""SUMMARY

        day()

        @Return:

        @Error:
        """
        return self._date.day

    @property
    def week(self, ):
        r"""SUMMARY

        week()

        @Return:

        @Error:
        """
        return WEEKDAY_JDIC.get(self._date.weekday())


def home(request):
    r"""SUMMARY

    home(request)

    @Arguments:
    - `request`:

    @Return:

    @Error:
    """
    context = {}
    now = datetime.datetime.now()
    context['today'] = Day(now)
    start = now - datetime.timedelta(PAST_COUNTS)
    end = now
    infos = list(Information.objects
                 .filter(publish=True)
                 .filter(pub_date__lte=now)
                 .order_by('-pub_date')[:MIN_INFO_COUNTS])
    range_infos = list(Information.objects
                       .filter(publish=True)
                       .filter(pub_date__gte=start)
                       .filter(pub_date__lte=end)
                       .order_by('-pub_date'))
    if len(infos) < len(range_infos):
        infos = range_infos
    context['info_list'] = [Info(i.title, i.category, i.pub_date, i.url) for i in infos]
    context['todayGarbageCollection'] = list(list_garbage_events(now, now))
    context['todaySchedules'] = list(list_main_events(now, now))
    context['todayHallBooking'] = list(list_hall_events(now, now))
    tomorrow = now + datetime.timedelta(1)
    context['tomorrowGarbageCollection'] = list(
        list_garbage_events(tomorrow, tomorrow))
    context['tomorrowSchedules'] = list(list_main_events(tomorrow, tomorrow))
    context['emergencies'] = list(Emergency.objects.filter(
        Q(expires_on__isnull=True)|Q(expires_on__gte=now),
        Q(published_from__isnull=True)|Q(published_from__lte=now),
        Q(status=True)).order_by('-published_from'))
    return render_to_response('home/home.html', context, context_instance=RequestContext(request))
