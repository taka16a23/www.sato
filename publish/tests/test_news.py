#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_news.py

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
from publish.models.news import NewsPostModel, NewsCategoryModel
import datetime


class TestNewsModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.category = NewsCategoryModel.objects.create(name='お知らせ')
        cls.now = datetime.datetime.now()
        cls.oneday = datetime.timedelta(1)

        super(TestNewsModel, cls).setUpClass()

    def setUp(self):
        super(TestNewsModel, self).setUp()

    def test_1week_5news_8minnews_10allnews(self, ):
        """
        1週間以内の news が5件以下でも過去のニュースとあわせて8件にする。
        """
        news_list = [('title1', datetime.datetime(2014, 1, 1)),
                     ('title2', datetime.datetime(2014, 2, 1)),
                     ('title3', datetime.datetime(2014, 3, 1)),
                     ('title4', datetime.datetime(2014, 4, 1)),
                     ('title5', datetime.datetime(2014, 5, 1)),
                     ('title6', datetime.datetime(2014, 6, 1)),
                     ('title7', datetime.datetime(2014, 7, 1)),
                     ('title8', datetime.datetime(2014, 8, 1)),
                     ('title9', datetime.datetime(2014, 9, 1)),
                     ('title10', datetime.datetime(2014, 10, 1)),
        ]
        for title, date in news_list:
            NewsPostModel.objects.create(
                title=title, category=self.category, url='http://localhost',
                publish_date=date)
        yestaday = self.now - self.oneday
        news_list2 = [
            ('title11', yestaday),
            ('title12', yestaday),
            ('title13', yestaday),
            ('title14', yestaday),
            ('title15', yestaday),
        ]
        for title, date in news_list2:
            NewsPostModel.objects.create(
                title=title, category=self.category, url='http://localhost',
                publish_date=date)
        self.assertEqual(NewsPostModel.objects.list_recently(
            recentdays=7, min_news_counts=8).count(), 8)

    def test_1week_10news_8minnews_10allnews(self, ):
        """
        1 週間以内の news すべてリスト化。10件
        """
        news_list = [('title1', datetime.datetime(2014, 1, 1)),
                     ('title2', datetime.datetime(2014, 2, 1)),
                     ('title3', datetime.datetime(2014, 3, 1)),
                     ('title4', datetime.datetime(2014, 4, 1)),
                     ('title5', datetime.datetime(2014, 5, 1)),
                     ('title6', datetime.datetime(2014, 6, 1)),
                     ('title7', datetime.datetime(2014, 7, 1)),
                     ('title8', datetime.datetime(2014, 8, 1)),
                     ('title9', datetime.datetime(2014, 9, 1)),
                     ('title10', datetime.datetime(2014, 10, 1)),
        ]
        for title, date in news_list:
            NewsPostModel.objects.create(
                title=title, category=self.category, url='http://localhost',
                publish_date=date)
        yestaday = self.now - self.oneday
        news_list2 = [
            ('title11', yestaday),
            ('title12', yestaday),
            ('title13', yestaday),
            ('title14', yestaday),
            ('title15', yestaday),
            ('title16', yestaday),
            ('title17', yestaday),
            ('title18', yestaday),
            ('title19', yestaday),
            ('title20', yestaday),
        ]
        for title, date in news_list2:
            NewsPostModel.objects.create(
                title=title, category=self.category, url='http://localhost',
                publish_date=date)
        self.assertEqual(NewsPostModel.objects.list_recently(
            recentdays=7, min_news_counts=8).count(), 10)

    def test_1week_3news_8minnews_3allnews(self, ):
        """
        1週間以内の news とそれ以前の news 合わせても8件以下でもエラーなく取り出す。
        """
        news_list = [('title1', datetime.datetime(2014, 1, 1)),
                     ('title2', datetime.datetime(2014, 2, 1)),
                     ('title3', datetime.datetime(2014, 3, 1)),
        ]
        for title, date in news_list:
            NewsPostModel.objects.create(
                title=title, category=self.category, url='http://localhost',
                publish_date=date)
        yestaday = self.now - self.oneday
        news_list2 = [
            ('title11', yestaday),
            ('title12', yestaday),
            ('title13', yestaday),
        ]
        for title, date in news_list2:
            NewsPostModel.objects.create(
                title=title, category=self.category, url='http://localhost',
                publish_date=date)
        self.assertEqual(NewsPostModel.objects.list_recently(
            recentdays=7, min_news_counts=8).count(), 6)

    def tearDown(self):
        super(TestNewsModel, self).tearDown()

    @classmethod
    def tearDownClass(cls, ):
        super(TestNewsModel, cls).tearDownClass()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_news.py ends here
