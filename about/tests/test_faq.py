#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_faq.py

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
from about.models.faq import QAModel, FAQ_STATUS_DRAFT, FAQ_STATUS_PUBLISHED


class TestFAQ(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestFAQ, cls).setUpClass()

    def setUp(self):
        self.objects = [
            QAModel.objects.create(question=u'test1', answer='test1', status=FAQ_STATUS_PUBLISHED),
            QAModel.objects.create(question=u'test2', answer='test1', status=FAQ_STATUS_PUBLISHED),
            QAModel.objects.create(question=u'test3', answer='test1', status=FAQ_STATUS_DRAFT),
            QAModel.objects.create(question=u'test4', answer='test1', status=FAQ_STATUS_DRAFT),
            QAModel.objects.create(question=u'test5', answer='test1', status=FAQ_STATUS_PUBLISHED),
            QAModel.objects.create(question=u'test6', answer='test1', status=FAQ_STATUS_DRAFT),
        ]
        super(TestFAQ, self).setUp()

    def test_publish(self, ):
        for obj in QAModel.objects.published():
            self.assertEqual(obj.status, FAQ_STATUS_PUBLISHED)

    def tearDown(self):
        super(TestFAQ, self).tearDown()

    @classmethod
    def tearDownClass(cls, ):
        super(TestFAQ, cls).tearDownClass()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_faq.py ends here
