#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_contact.py

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
from django.test import TestCase, Client
from about.models import ContactReceiverModel
from about.models import ContactedModel
from django.core import mail


class TestContactReceiver(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestContactReceiver, cls).setUpClass()

    def setUp(self):
        ContactReceiverModel.objects.create(
            name='example', email='example@example.com', active=True)
        ContactReceiverModel.objects.create(
            name='example', email='example@example.com', active=False)
        ContactReceiverModel.objects.create(
            name='example', email='example@example.com', active=True)

    def test_active(self, ):
        for obj in ContactReceiverModel.objects.active():
            self.assertTrue(obj.active)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        super(TestContactReceiver, cls).tearDownClass()


class TestContactedModel(TestCase):
    """2016/03/10"""
    @classmethod
    def setUpClass(cls):
        super(TestContactedModel, cls).setUpClass()

    def setUp(self):
        self.client = Client()

    def test_notify(self):
        self.skipTest('')
        obj = ContactedModel.objects.create(
            name=u'田中美里', email='example@example.com', body=u'内容')
        subject = 'this is subject'
        obj.send_notify(subject)
        self.assertEqual(len(mail.outbox), 1)

    def test_page(self, ):
        response = self.client.get('/about/solve/')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        super(TestContactedModel, self).tearDown()

    @classmethod
    def tearDownClass(cls, ):
        super(TestContactedModel, cls).tearDownClass()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_contact.py ends here
