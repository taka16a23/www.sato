#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_board.py

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
import os
from django.test import TestCase
from publish.models.board import DocumentModel
from django.forms import forms
from django.core.files import File

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(CURRENT_DIR, 'sample.pdf')
DOC_PATH = os.path.join(CURRENT_DIR, 'sample.doc')
JPG_PATH = os.path.join(CURRENT_DIR, 'sample.jpg')


class TestBoardModel(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestBoardModel, cls).setUpClass()

    def setUp(self):
        super(TestBoardModel, self).setUp()

    def test_create(self, ):
        # valid
        obj = DocumentModel.objects.create(title='tes', file=File(open(PDF_PATH, 'rb')))
        self.assertTrue(bool(obj.file))
        self.assertTrue(bool(obj.thumbnail))
        self.assertTrue(bool(obj.publish_date))

    def test_unicode_title(self, ):
        obj = DocumentModel.objects.create(title=u'日本語', file=File(open(PDF_PATH, 'rb')))
        self.assertTrue(bool(obj.file))
        self.assertTrue(bool(obj.thumbnail))
        self.assertTrue(bool(obj.publish_date))

    def tearDown(self):
        super(TestBoardModel, self).tearDown()

    @classmethod
    def tearDownClass(cls, ):
        super(TestBoardModel, cls).tearDownClass()


# with self.assertRaises(forms.ValidationError):
#     DocumentModel.objects.create(title='tes', file=File(open(DOC_PATH, 'rb')))
# with self.assertRaises(forms.ValidationError):
#     DocumentModel.objects.create(title='tes', file=File(open(JPG_PATH, 'rb')))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_board.py ends here
