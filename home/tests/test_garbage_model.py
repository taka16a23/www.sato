#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_garbage_model.py

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
from home.models import GarbageEvent
from home.models import EVENT_CONFIRMED_STATUS, EVENT_TENTATIVE_STATUS, EVENT_CANCELLED_STATUS

import datetime


class TestGarbageModel(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestGarbageModel, cls).setUpClass()

    def setUp(self):
        self.events = [
            # yesterday
            GarbageEvent.objects.create(gid=u'la37fjqc2hanfviv29jls0fm5g_20160307', summary='かん', date=datetime.datetime.now() - datetime.timedelta(1), url='http://localhost/', status=EVENT_CONFIRMED_STATUS),
            GarbageEvent.objects.create(gid=u'la37fjqc2hanfviv29jls0fm5a_20160307', summary='かん', date=datetime.datetime.now() - datetime.timedelta(1), url='http://localhost/', status=EVENT_CANCELLED_STATUS),
            # today
            GarbageEvent.objects.create(gid=u'la37fjqc2hanfviv29jls0fm5g_20160308', summary='紙ごみ', date=datetime.datetime.now(), url='http://localhost/', status=EVENT_CONFIRMED_STATUS),
            GarbageEvent.objects.create(gid=u'la37fjqc2hanfviv29jls0fm5a_20160308', summary='紙ごみ', date=datetime.datetime.now(), url='http://localhost/', status=EVENT_CANCELLED_STATUS),
            # tomorrow
            GarbageEvent.objects.create(gid=u'la37fjqc2hanfviv29jls0fm5g_20160309', summary='燃やせるごみ', date=datetime.datetime.now() + datetime.timedelta(1), url='http://localhost/', status=EVENT_CONFIRMED_STATUS),
            GarbageEvent.objects.create(gid=u'la37fjqc2hanfviv29jls0fm5a_20160309', summary='燃やせるごみ', date=datetime.datetime.now() + datetime.timedelta(1), url='http://localhost/', status=EVENT_CANCELLED_STATUS),
        ]
        super(TestGarbageModel, self).setUp()

    def test_garbage_today(self, ):
        objects = GarbageEvent.objects.confirmed().filter(date=datetime.datetime.now())
        self.assertEqual(objects.count(), 1)
        self.assertEqual(objects[0].status, EVENT_CONFIRMED_STATUS)

    def test_garbage_tomorrow(self, ):
        objects = GarbageEvent.objects.confirmed().filter(
            date=datetime.datetime.now() + datetime.timedelta(1))
        self.assertEqual(objects.count(), 1)
        self.assertEqual(objects[0].status, EVENT_CONFIRMED_STATUS)

    def tearDown(self):
        super(TestGarbageModel, self).tearDown()

    @classmethod
    def tearDownClass(cls, ):
        super(TestGarbageModel, cls).tearDownClass()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_garbage_model.py ends here
