#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess as sbp
import tempfile
import contextlib
import shutil
import datetime

from BeautifulSoup import BeautifulSoup
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from django.forms import forms
from django.core.files import File

from core.models import DisplayableModel
from core.managers import DisplayableManager, DisplayableQuerySet, ManagerAbstract


##########
# 回覧板 #
##########
def validate_file_pdf(value):
    r"""SUMMARY

    validate_file_pdf(values)

    @Arguments:
    - `values`:

    @Return:

    @Error:
    """
    # TODO: (Atami) [2016/02/16]
    # validate pdf
    if not hasattr(value.file, 'content_type'):
        return
    if value.file.content_type != 'application/pdf':
        raise forms.ValidationError(u'Not PDF')

@contextlib.contextmanager
def tempdir(prefix='tmp'):
    """A context manager for creating and then deleting a temporary directory."""
    tmpdir = tempfile.mkdtemp(prefix=prefix)
    try:
        yield tmpdir
    finally:
        shutil.rmtree(tmpdir)


class DocumentModel(DisplayableModel):
    r"""DocumentModel

    DocumentModel is a DisplayableModel.
    Responsibility:
    """
    objects = DisplayableManager()

    title = models.CharField(u'タイトル', max_length=255)
    file = models.FileField(
        upload_to='boards/',
        validators=[validate_file_pdf],
        null=False, blank=False)
    thumbnail = models.ImageField(
        u'サムネイル',
        upload_to='boards/',
        blank=True, null=True)

    def make_thumbnail(self, ):
        r"""SUMMARY

        make_thumbnail()

        @Return:

        @Error:
        """
        # TODO: (Atami) [2016/02/08]
        # refactaring and logging
        f_name = os.path.basename(unicode(self.file))
        im_name = os.path.splitext(f_name)[0] + '.jpg'
        with tempdir() as tmppath:
            self.file.seek(0)
            copied = tempfile.NamedTemporaryFile(mode='wb')
            copied.write(self.file.read())
            copied.flush()
            im_path = os.path.join(tmppath, 'thumbnail.jpg')
            cmdline = (
                u'/usr/bin/convert -resize 200x200 -alpha remove %s[0] %s'
                % (copied.name, im_path))
            try:
                print(cmdline)
                sbp.check_call(cmdline, shell=True,
                               stdin=sbp.PIPE, stdout=sbp.PIPE, stderr=sbp.PIPE)
                with open(im_path, 'rb') as fobj:
                    self.thumbnail.save(im_name, File(fobj), save=False)
            except sbp.CalledProcessError as err:
                print(err)

    def save(self, ):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        try:
            self.make_thumbnail()
        except StandardError as err:
            print(err)
        super(DocumentModel, self).save()

    class Meta:
        verbose_name = u'回覧物'
        verbose_name_plural = u'回覧物'

    def __unicode__(self):
        return self.title


############
# 活動報告 #
############

class ActivityPostModel(DisplayableModel):
    r"""ActivityPostModel

    ActivityPostModel is a models.Model.
    Responsibility:
    """
    objects = DisplayableManager()

    class Meta:
        verbose_name = u'活動報告'
        verbose_name_plural = u'活動報告'

    title = models.CharField(u'題名', max_length=200)
    body = RichTextUploadingField(u'本文', blank=True, null=True)
    description = models.TextField(u'記事の説明', blank=True, null=True)

    def save(self, *args, **kwargs):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        text = u''
        try:
            text = u''.join(BeautifulSoup(self.body).findAll(text=True))
        except Exception as err:
            # TODO: (Atami) [2016/02/17]
            print(err)
        self.description = text[:300]
        super(ActivityPostModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


########
# news #
########

NEWS_IMPORTANT = 1
NEWS_INFORMATION = 2
NEWS_SECURITY = 3
NEWS_ACTIVITY = 4
NEWS_WANTED = 5
NEWS_UPDATE = 6

NEWS_CATEGORIES = (
    (NEWS_IMPORTANT, u'重要'),
    (NEWS_INFORMATION, u'お知らせ'),
    (NEWS_SECURITY, u'防犯'),
    (NEWS_ACTIVITY, u'ご報告'),
    (NEWS_WANTED, u'募集'),
    (NEWS_UPDATE, u'更新'),
)

NEWS_CATEGORIES_DIC = {integer: name for integer, name in NEWS_CATEGORIES}

CATEGORY_CLASS_KEYS = {
    NEWS_IMPORTANT: 'categoryImportant',
    NEWS_INFORMATION: 'categoryInfo',
    NEWS_SECURITY: 'categorySecurity',
    NEWS_ACTIVITY: 'categoryReport',
    NEWS_WANTED: 'categoryWanted',
    NEWS_UPDATE: 'categoryUpdate',
}

MIN_NEWS_COUNTS = 8


class NewsPostQuerySet(DisplayableQuerySet):
    r"""NewsPostQuerySet

    NewsPostQuerySet is a DisplayableQuerySet.
    Responsibility:
    """
    def latest_by_days(self, days, min_news_counts=MIN_NEWS_COUNTS):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        end = now = datetime.datetime.now()
        start = now - datetime.timedelta(days)
        news = self.published().order_by('-publish_date')[:min_news_counts]
        rangenews = self.range_by_publish_date(start, end).order_by('-publish_date')
        if len(news) < len(rangenews):
            return rangenews
        return news


class NewsPostManager(ManagerAbstract):
    r"""NewsPostManager

    NewsPostManager is a ManagerAbstract.
    Responsibility:
    """
    def get_query_set(self, ):
        r"""SUMMARY

        get_query_set()

        @Return:

        @Error:
        """
        return NewsPostQuerySet(self.model)


class NewsPostModel(DisplayableModel):
    r"""NewsPostModel

    NewsPostModel is a DisplayableModel.
    Responsibility:
    """
    objects = NewsPostManager()

    title = models.CharField(u'タイトル', max_length=200, blank=False)
    category = models.IntegerField(
        u'お知らせの種類',
        choices=NEWS_CATEGORIES,
        blank=False, default=2)
    url = models.URLField('URL', max_length=200, blank=False)

    class Meta:
        verbose_name = u'お知らせ'
        verbose_name_plural = u'お知らせ'

    def __unicode__(self):
        return unicode(self.title)

    def as_class_key(self, ):
        r"""SUMMARY

        as_class_key()

        @Return:

        @Error:
        """
        return CATEGORY_CLASS_KEYS.get(self.category)

    def as_category_name(self, ):
        r"""SUMMARY

        as_category_name()

        @Return:

        @Error:
        """
        return NEWS_CATEGORIES_DIC.get(self.category, u'')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
