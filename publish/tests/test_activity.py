#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_activity.py

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
from publish.models.activity import ActivityPostModel, TagModel
from datetime import *
from core.models import DISPLAY_STATUS_PUBLISHED, DISPLAY_STATUS_DRAFT


class TestActivityPostModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.now = datetime.now()
        cls.testtag = TagModel.objects.create(name='testtag')
        cls.create = ActivityPostModel.objects.create
        super(TestActivityPostModel, cls).setUpClass()

    def setUp(self):
        oneday = timedelta(1)
        self.evnts = [
            # self.create(title=u'公開日2014年1月1日',
                   # publish_date=datetime(2014, 1, 1),
                   # status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日2014年1月1日終日',
                   publish_date=datetime(2014, 1, 1),
                   expiry_date=datetime.combine(datetime(2014, 1, 1), time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日2014年1月1日有効期限2015年3月31日',
                   publish_date=datetime(2014, 1, 1),
                   expiry_date=datetime.combine(datetime(2015, 3, 31), time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日2014年12月31日23時59分9999秒',
                   publish_date=datetime.combine(datetime(2014, 12, 31), time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日2014年12月31日有効期限2015年1月3日', # 年跨ぎ
                   publish_date=datetime(2014, 12, 31),
                   expiry_date=datetime.combine(datetime(2015, 1, 3), time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日2014年3月31日有効期限2014年4月3日', # 年度跨ぎ
                   publish_date=datetime(2014, 3, 31),
                   expiry_date=datetime.combine(datetime(2015, 4, 3), time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日2014年1月1日08:00有効期限2014年1月1日12:00',
                   publish_date=datetime(2014, 1, 1, 8),
                   expiry_date=datetime(2014, 1, 1, 12),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日2015年3月15日',
                   publish_date=datetime(2015, 3, 15),
                   status=DISPLAY_STATUS_PUBLISHED),
            # self.create(title=u'公開日本日',
            #        publish_date=self.now,
            #        status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'公開日本日当時刻、有効期限3時間後',
                   publish_date=self.now,
                   expiry_date=self.now + timedelta(hours=3),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'本日終日',
                   publish_date=datetime.combine(self.now, time.min),
                   expiry_date=datetime.combine(self.now, time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'今日から明日2日間',
                   publish_date=datetime.combine(self.now, time.min),
                   expiry_date=datetime.combine(self.now + oneday, time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            self.create(title=u'今年初め～終わりまで',
                   publish_date=datetime.combine(datetime(self.now.year, 1, 1), time.min),
                   expiry_date=datetime.combine(datetime(self.now.year, 12, 31), time.max),
                   status=DISPLAY_STATUS_PUBLISHED),
            # draft copied
            # self.create(title=u'公開日2014年1月1日',
            #        publish_date=datetime(2014, 1, 1),
            #        status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日2014年1月1日終日',
                   publish_date=datetime(2014, 1, 1),
                   expiry_date=datetime.combine(datetime(2014, 1, 1), time.max),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日2014年1月1日有効期限2015年3月31日',
                   publish_date=datetime(2014, 1, 1),
                   expiry_date=datetime.combine(datetime(2015, 3, 31), time.max),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日2014年12月31日23時59分9999秒',
                   publish_date=datetime.combine(datetime(2014, 12, 31), time.max),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日2014年12月31日有効期限2015年1月3日', # 年跨ぎ
                   publish_date=datetime(2014, 12, 31),
                   expiry_date=datetime.combine(datetime(2015, 1, 3), time.max),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日2014年3月31日有効期限2014年4月3日', # 年度跨ぎ
                   publish_date=datetime(2014, 3, 31),
                   expiry_date=datetime.combine(datetime(2015, 4, 3), time.max),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日2014年1月1日08:00有効期限2014年1月1日12:00',
                   publish_date=datetime(2014, 1, 1, 8),
                   expiry_date=datetime(2014, 1, 1, 12),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日2015年3月15日',
                   publish_date=datetime(2015, 3, 15),
                   status=DISPLAY_STATUS_DRAFT),
            # self.create(title=u'公開日本日',
            #        publish_date=self.now,
            #        status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日本日当時刻、有効期限3時間後',
                   publish_date=self.now - timedelta(hours=1),
                   expiry_date=self.now + timedelta(hours=3),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'公開日今日',
                   publish_date=datetime.combine(self.now, time.min),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'本日終日',
                   publish_date=datetime.combine(self.now, time.min),
                   expiry_date=datetime.combine(self.now, time.max),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'今日から明日2日間',
                   publish_date=datetime.combine(self.now, time.min),
                   expiry_date=datetime.combine(self.now + oneday, time.max),
                   status=DISPLAY_STATUS_DRAFT),
            self.create(title=u'今年初め～終わりまで',
                   publish_date=datetime.combine(datetime(self.now.year, 1, 1), time.min),
                   expiry_date=datetime.combine(datetime(self.now.year, 12, 31), time.max),
                   status=DISPLAY_STATUS_DRAFT),
        ]
        obj = self.create(title=u'公開日今日',
                     publish_date=datetime.combine(self.now, time.min),
                     status=DISPLAY_STATUS_PUBLISHED)
        obj.save()
        obj.tags.add(self.testtag)
        obj.save()
        obj2 = self.create(title=u'公開日今日',
                      publish_date=datetime.combine(self.now, time.min),
                      status=DISPLAY_STATUS_DRAFT)
        obj2.save()
        obj2.tags.add(self.testtag)
        obj2.save()
        obj3 = self.create(title=u'公開日2014年1月1日',
                     publish_date=datetime(2014, 1, 1),
                     status=DISPLAY_STATUS_PUBLISHED)
        obj3.save()
        obj3.tags.add(self.testtag)
        obj3.save()
        obj4 = self.create(title=u'公開日2014年1月1日',
                      publish_date=datetime(2014, 1, 1),
                      status=DISPLAY_STATUS_DRAFT)
        obj4.save()
        obj4.tags.add(self.testtag)
        obj4.save()
        super(TestActivityPostModel, self).setUp()

    def test_yealy_filter(self, ):
        objects = ActivityPostModel.objects.published().by_year(2014)
        self.assertEqual(objects.count(), 2)
        objects2 = ActivityPostModel.objects.published().by_year(self.now.year)
        self.assertEqual(objects2.count(), 5)

    def test_tag_and_year(self, ):
        self.skipTest('Not Implemented')

    # def test_auto_tagging(self, ):
    #     obj = self.create(title=u'公開日2014年1月1日',
    #                   publish_date=datetime(2014, 1, 1),
    #                   status=DISPLAY_STATUS_DRAFT)
    #     obj.save()
    #     print('DEBUG-1-test_activity.py')
    #     tag = TagModel.objects.get_or_create(name=u'2014年度')
    #     print('DEBUG-2-test_activity.py')
    #     print(obj.tags)
    #     self.assertTrue(tag in list(obj.tags))

    def test_by_tag(self, ):
        objects = ActivityPostModel.objects.published().by_tagname('testtag')
        self.assertEqual(objects.count(), 2)

    def tearDown(self):
        super(TestActivityPostModel, self).tearDown()

    @classmethod
    def tearDownClass(cls, ):
        super(TestActivityPostModel, cls).tearDownClass()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_activity.py ends here
