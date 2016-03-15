#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_mainevent.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubset', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual',
 'assertIdentical', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
 'assertIsNot', 'assertIsNotInstance', 'assertIsNotNone', 'assertItemsEqual',
 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMethodsMatch',
 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals',
 'assertNotApproximates', 'assertNotEndsWith', 'assertNotEqual',
 'assertNotEquals', 'assertNotIdentical', 'assertNotIn', 'assertNotIsInstance',
 'assertNotRegexpMatches', 'assertNotStartsWith', 'assertRaises',
 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual',
 'assertSetEqual', 'assertStartsWith', 'assertTrue', 'assertTupleEqual', ]

['failIf', 'failIfAlmostEqual', 'failIfApproximates', 'failIfEndsWith',
 'failIfEqual', 'failIfIdentical', 'failIfIn', 'failIfIs', 'failIfIsInstance',
 'failIfStartsWith', 'failUnless', 'failUnlessAlmostEqual',
 'failUnlessApproximates', 'failUnlessEndsWith', 'failUnlessEqual',
 'failUnlessIdentical', 'failUnlessIn', 'failUnlessIs', 'failUnlessIsInstance',
 'failUnlessMethodsMatch', 'failUnlessRaises', 'failUnlessRaisesRegexp',
 'failUnlessStartsWith', 'failureException', ]

"""
from django.test import TestCase
from home.models import MainEvent
from home.models import EVENT_CONFIRMED_STATUS, EVENT_TENTATIVE_STATUS, EVENT_CANCELLED_STATUS
import datetime


class TestMainEvent(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.now = datetime.datetime.now()
        cls.yestarday = cls.now - datetime.timedelta(1)
        cls.tomorrow = cls.now + datetime.timedelta(1)
        super(TestMainEvent, cls).setUpClass()

    def setUp(self):
        self.events = [
            MainEvent.objects.create(gid=u'yestarday_confirmed', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.yestarday.year, self.yestarday.month, self.yestarday.day, hour=9), end=datetime.datetime(self.yestarday.year, self.yestarday.month, self.yestarday.day, hour=12), status=EVENT_CONFIRMED_STATUS),
            MainEvent.objects.create(gid=u'yestarday_cancelled', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.yestarday.year, self.yestarday.month, self.yestarday.day, hour=9), end=datetime.datetime(self.yestarday.year, self.yestarday.month, self.yestarday.day, hour=12), status=EVENT_CANCELLED_STATUS),
            MainEvent.objects.create(gid=u'yestarday_to_today_confirmed', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.yestarday.year, self.yestarday.month, self.yestarday.day, hour=9), end=datetime.datetime(self.now.year, self.now.month, self.now.day, hour=12), status=EVENT_CONFIRMED_STATUS),
            MainEvent.objects.create(gid=u'today_confirmed', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.now.year, self.now.month, self.now.day, hour=9), end=datetime.datetime(self.now.year, self.now.month, self.now.day, hour=12), status=EVENT_CONFIRMED_STATUS),
            MainEvent.objects.create(gid=u'today_cancelled', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.now.year, self.now.month, self.now.day, hour=9), end=datetime.datetime(self.now.year, self.now.month, self.now.day, hour=12), status=EVENT_CANCELLED_STATUS),
            MainEvent.objects.create(gid=u'tomorrow_confirmed', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.tomorrow.year, self.tomorrow.month, self.tomorrow.day, hour=9), end=datetime.datetime(self.tomorrow.year, self.tomorrow.month, self.tomorrow.day, hour=12), status=EVENT_CONFIRMED_STATUS),
            MainEvent.objects.create(gid=u'tomorrow_confirmedPM', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.tomorrow.year, self.tomorrow.month, self.tomorrow.day, hour=12), end=datetime.datetime(self.tomorrow.year, self.tomorrow.month, self.tomorrow.day, hour=18), status=EVENT_CONFIRMED_STATUS),
            MainEvent.objects.create(gid=u'tomorrow_cancelled', summary='summary', description='desc', created=self.now, modified=self.now, url='http://localhost/', start=datetime.datetime(self.tomorrow.year, self.tomorrow.month, self.tomorrow.day, hour=9), end=datetime.datetime(self.tomorrow.year, self.tomorrow.month, self.tomorrow.day, hour=12), status=EVENT_CANCELLED_STATUS),
        ]
        super(TestMainEvent, self).setUp()

    def test_mainevent_today(self, ):
        start = datetime.datetime.combine(self.now, datetime.time.min)
        end = datetime.datetime.combine(self.now, datetime.time.max)
        objects = MainEvent.objects.between_events(start, end).confirmed()
        self.assertEqual(objects.count(), 2)
        self.assertEqual(objects[0].status, EVENT_CONFIRMED_STATUS)
        self.assertEqual(objects[1].status, EVENT_CONFIRMED_STATUS)

    def test_mainevent_tomorrow(self, ):
        start = datetime.datetime.combine(self.tomorrow, datetime.time.min)
        end = datetime.datetime.combine(self.tomorrow, datetime.time.max)
        objects = MainEvent.objects.between_events(start, end).confirmed()
        self.assertEqual(objects.count(), 2)
        self.assertEqual(objects[0].status, EVENT_CONFIRMED_STATUS)
        self.assertEqual(objects[1].status, EVENT_CONFIRMED_STATUS)

    def tearDown(self):
        super(TestMainEvent, self).tearDown()

    @classmethod
    def tearDownClass(cls, ):
        super(TestMainEvent, cls).tearDownClass()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_mainevent.py ends here
