#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""controllers -- DESCRIPTION

"""
from sato.settings import BASE_DIR, STATIC_ROOT
from home.models import GarbageEvent, MainEvent, HallEvent
from home.models import EVENT_STATUS_DICT, EVENT_CANCELLED_STATUS

import os
import collections
import datetime

from dateutil import parser as dateparser
from dateutil.relativedelta import relativedelta
import httplib2
import oauth2client
import apiclient

CREDENTIAL_DIR = os.path.join(BASE_DIR, '.credentials')
if not os.path.exists(CREDENTIAL_DIR):
    os.makedirs(CREDENTIAL_DIR)
GOOGLE_CALENDAR_JSON_FILE_NAME = 'calendar-python-quickstart.json'
GOOGLE_CALENDAR_JSON_FILE_PATH = os.path.join(
    CREDENTIAL_DIR, GOOGLE_CALENDAR_JSON_FILE_NAME)

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = os.path.join(STATIC_ROOT, 'client_secret.json')
APPLICATION_NAME = 'Google Calendar API Python Quickstart'
Namespace = collections.namedtuple(
    'Namespace', ('auth_host_name', 'auth_host_port', 'logging_level',
                  'noauth_local_webserver'))

CALID_MAIN = 'satotanakami@gmail.com'
CALID_GARBAGE = 'c9uc1q8uiftrf0agsvvbpo6dvc@group.calendar.google.com'
CALID_HALL = '6m5ne5kcfmkek4t0ba37o95olo@group.calendar.google.com'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    store = oauth2client.file.Storage(GOOGLE_CALENDAR_JSON_FILE_PATH)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = oauth2client.client.flow_from_clientsecrets(
            CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        flags = Namespace(auth_host_name='localhost', auth_host_port=[8080, 8090],
                          logging_level='ERROR', noauth_local_webserver=False)
        # if flags:
        credentials = oauth2client.tools.run_flow(flow, store, flags)
        # else: # Needed only for compatibility with Python 2.6
            # credentials = tools.run(flow, store)
        print('Storing credentials to ' + GOOGLE_CALENDAR_JSON_FILE_PATH)
    return credentials


def get_service():
    r"""SUMMARY

    get_service()

    @Return:

    @Error:
    """
    try:
        credentials = get_credentials()
    except AttributeError as err:
        print(err)
        return None
    return apiclient.discovery.build(
        'calendar', 'v3', http=credentials.authorize(httplib2.Http()))


def list_events(calid, time_min=None, max_results=250, showdeleted=True):
    r"""SUMMARY

    list_events(calid, time_min=None, max_results=250, showdeleted=True)

    @Arguments:
    - `calid`:
    - `start`:
    - `counts`:
    - `showdeleted`:

    @Return:

    @Error:
    """
    service = get_service()
    return service.events().list(
        calendarId=calid,
        timeMin=time_min.isoformat() + 'Z',
        maxResults=max_results,
        singleEvents=True,
        showDeleted=showdeleted,
        orderBy='startTime')


def is_allday(event):
    r"""SUMMARY

    is_allday(event)

    @Arguments:
    - `event`:

    @Return:

    @Error:
    """
    return 'start' in event and 'date' in event['start']


def list_garbage_allday_events(start=None, counts=250, showdeleted=True):
    r"""SUMMARY

    list_garbage_allday_events(start, counts=250, showdeleted=True)

    @Arguments:
    - `start`: if None will set datetime.datetime.utcnow.
    - `max_results`: 250 is google default

    @Return:

    @Error:
    """
    start = start or datetime.datetime.utcnow()
    events = list_events(
        calid=CALID_GARBAGE, time_min=start, max_results=counts,
        showdeleted=showdeleted).execute().get('items', [])
    # filter for only allday
    return [e for e in events if is_allday(e)]


def sync_garbage_calendar(start=None, counts=250):
    r"""SUMMARY

    sync_garbage_calendar()

    @Return:

    @Error:
    """
    events = list_garbage_allday_events(start=start, counts=counts)
    for event in events:
        defaults = {}
        defaults['gid'] = event['id']
        defaults['summary'] = event['summary']
        defaults['date'] = datetime.datetime.strptime(
            event['start']['date'], '%Y-%m-%d').date()
        defaults['url'] = event['htmlLink']
        defaults['status'] = EVENT_STATUS_DICT.get(
            event['status'], EVENT_CANCELLED_STATUS)
        model, created = GarbageEvent.objects.get_or_create(
            gid=event['id'], defaults=defaults)
        if created:
            print(u'created {0.gid} {0.date} {0.summary}'.format(model))
            continue
        print(u'updating {0.gid} {0.date} {0.summary}'.format(model))
        # update
        model.gid = defaults['gid']
        model.summary = defaults['summary']
        model.date = defaults['date']
        model.url = defaults['url']
        model.status = defaults['status']
        model.save()


def list_main_events(start=None, counts=250, showdeleted=True):
    r"""SUMMARY

    @Arguments:
    - `start`:
    - `counts`:
    - `showdeleted`:

    @Return:

    list_main_events(start=None, counts=250, showdeleted=True)

    @Error:
    """
    start = start or datetime.datetime.utcnow() - relativedelta(days=2)
    return list_events(
        calid=CALID_MAIN, time_min=start, max_results=counts,
        showdeleted=showdeleted).execute().get('items', [])


def sync_main_calendar(start=None, counts=250):
    r"""SUMMARY

    sync_main_calendar(start=None,counts=250)

    @Arguments:
    - `start`:
    - `counts`:

    @Return:

    @Error:
    """
    events = list_main_events(start=start, counts=counts)
    for event in events:
        defaults = {}
        defaults['gid'] = event['id']
        defaults['summary'] = event['summary']
        defaults['description'] = event.get('description', '')
        defaults['url'] = event['htmlLink']
        try:
            defaults['created'] = dateparser.parse(
                event['created']).replace(tzinfo=None)
        except ValueError as err:
            print(event['created'])
            defaults['created'] = datetime.datetime.now()
        defaults['modified'] = dateparser.parse(
            event['updated']).replace(tzinfo=None)
        defaults['status'] = EVENT_STATUS_DICT.get(
            event['status'], EVENT_CANCELLED_STATUS)
        if is_allday(event):
            start = datetime.datetime.strptime(event['start']['date'], '%Y-%m-%d')
            defaults['start'] = start
            defaults['end'] = datetime.datetime.combine(start, datetime.time.max)
        else:
            defaults['start'] = dateparser.parse(
                event['start']['dateTime']).replace(tzinfo=None)
            defaults['end'] = dateparser.parse(
                event['end']['dateTime']).replace(tzinfo=None)
        print(defaults['start'])
        model, created = MainEvent.objects.get_or_create(
            gid=event['id'], defaults=defaults)
        if created:
            print(u'created {0.gid} {0.start}:{0.end} {0.summary}'.format(model))
            continue
        print(u'updating {0.gid} {0.start}:{0.end} {0.summary}'.format(model))
        # update
        model.gid = defaults['gid']
        model.summary = defaults['summary']
        model.description = defaults['description']
        model.start = defaults['start']
        model.end = defaults['end']
        model.url = defaults['url']
        model.created = defaults['created']
        model.modified = defaults['modified']
        model.status = defaults['status']
        model.save()


def list_hall_events(start=None, counts=250, showdeleted=True):
    r"""SUMMARY

    @Arguments:
    - `start`:
    - `counts`:
    - `showdeleted`:

    @Return:

    list_hall_events(start=None, counts=250, showdeleted=True)

    @Error:
    """
    start = start or datetime.datetime.utcnow() - relativedelta(days=2)
    return list_events(
        calid=CALID_HALL, time_min=start, max_results=counts,
        showdeleted=showdeleted).execute().get('items', [])


def sync_hall_calendar(start=None,counts=250):
    r"""SUMMARY

    sync_hall_calendar(start=None,counts=250)

    @Arguments:
    - `start`:
    - `counts`:

    @Return:

    @Error:
    """
    events = list_hall_events(start=start, counts=counts)
    for event in events:
        defaults = {}
        defaults['gid'] = event['id']
        defaults['summary'] = event['summary']
        defaults['description'] = event.get('description', '')
        defaults['url'] = event['htmlLink']
        try:
            defaults['created'] = dateparser.parse(
                event['created']).replace(tzinfo=None)
        except ValueError as err:
            print(event['created'])
            defaults['created'] = datetime.datetime.now()
        defaults['modified'] = dateparser.parse(
            event['updated']).replace(tzinfo=None)
        defaults['status'] = EVENT_STATUS_DICT.get(
            event['status'], EVENT_CANCELLED_STATUS)
        if is_allday(event):
            start = datetime.datetime.strptime(event['start']['date'], '%Y-%m-%d')
            defaults['start'] = start
            defaults['end'] = datetime.datetime.combine(start, datetime.time.max)
        else:
            defaults['start'] = dateparser.parse(
                event['start']['dateTime']).replace(tzinfo=None)
            defaults['end'] = dateparser.parse(
                event['end']['dateTime']).replace(tzinfo=None)
        model, created = HallEvent.objects.get_or_create(
            gid=event['id'], defaults=defaults)
        if created:
            print(u'created {0.gid} {0.start}:{0.end} {0.summary}'.format(model))
            continue
        print(u'updating {0.gid} {0.start}:{0.end} {0.summary}'.format(model))
        # update
        model.gid = defaults['gid']
        model.summary = defaults['summary']
        model.description = defaults['description']
        model.start = defaults['start']
        model.end = defaults['end']
        model.url = defaults['url']
        model.created = defaults['created']
        model.modified = defaults['modified']
        model.status = defaults['status']
        model.save()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# controllers.py ends here
