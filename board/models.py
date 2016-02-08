#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import forms
from django.db.models.signals import post_save
from django.core.files import File

import uuid
import os
import datetime
from sato import settings
import subprocess as sbp
import hashlib
import tempfile
import contextlib
import shutil


def get_hash_name(fobj):
    r"""SUMMARY

    get_hash_name(fobj)

    @Arguments:
    - `fobj`:

    @Return:

    @Error:
    """
    fobj.seek(0)
    md5 = hashlib.md5()
    if fobj.multiple_chunks():
        md5.update(fobj.chunks())
    else:
        md5.update(fobj.read())
    fobj.seek(0)
    return md5.hexdigest()


def get_file_path(instance, filename):
    return os.path.join('boards', get_hash_name(instance.file) + '.pdf')

def validate_file_pdf(value):
    r"""SUMMARY

    validate_file_pdf(values)

    @Arguments:
    - `values`:

    @Return:

    @Error:
    """
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


STATUS = ((False, u'下書き'),
          (True, u'公開する'))


# Create your models here.
class Board(models.Model):
    r"""Board

    Board is a models.Model.
    Responsibility:
    """
    title = models.CharField(u'タイトル', max_length=255)
    # slug = models.CharField(u'Slug', max_length=255, unique=True)
    file = models.FileField(
        upload_to='boards/',
        validators=[validate_file_pdf],
        null=False, blank=False)
    thumbnail = models.ImageField(
        u'サムネイル',
        upload_to='boards/',
        blank=True, null=True)
    published_from = models.DateTimeField(
        u'公開開始',
        help_text=u'公開を選択すると、ここで設定した日時までは公開されません',
        default=datetime.datetime.now)
    expires_on = models.DateTimeField(
        u'有効期限',
        help_text=u'公開を選択すると、ここで設定した日時以降は公開されません',
        blank=True, null=True)
    status = models.BooleanField(
        help_text=u'下書きを選択すると、サイトの管理ユーザーのみが見られる状態になります。',
        choices=STATUS,
        default=True)

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
            # fpath = os.path.join(tmppath, f_name)
            self.file.seek(0)
            print('DEBUG-8-models.py')
            copied = tempfile.NamedTemporaryFile(mode='wb')
            print('DEBUG-9-models.py')
            copied.write(self.file.read())
            print('DEBUG-10-models.py')
            copied.flush()
            # copied.close()
            print('DEBUG-11-models.py')
            im_path = os.path.join(tmppath, 'thumbnail.jpg')
            print('DEBUG-12-models.py')
            cmdline = (
                u'/usr/bin/convert -resize 200x200 -alpha remove %s[0] %s'
                % (copied.name, im_path))
            print('DEBUG-13-models.py')
            try:
                print('DEBUG-15-models.py')
                print(cmdline)
                sbp.check_call(cmdline, shell=True,
                               stdin=sbp.PIPE, stdout=sbp.PIPE, stderr=sbp.PIPE)
                print('DEBUG-14-models.py')
                with open(im_path, 'rb') as fobj:
                    self.thumbnail.save(im_name, File(fobj), save=False)
            except sbp.CalledProcessError as err:
                print('DEBUG-7-models.py')
                print(err)

    def save(self, ):
        r"""SUMMARY

        save()

        @Return:

        @Error:
        """
        # ifname = open('/root/work/teswww/pdf-sample.jpg', 'rb')
        # self.thumbnail.save(File(ifname))
        # fname = os.path.splitext(os.path.basename(self.file.name))[0]
        # self.thumbnail = os.path.join('boards', fname + '.png')
        print('DEBUG-2-models.py')
        print(self.file.path)
        print('DEBUG-3-models.py')
        try:
            self.make_thumbnail()
        except StandardError as err:
            print('DEBUG-6-models.py')
            print(err)
            print(type(err))
        super(Board, self).save()
        print('DEBUG-4-models.py')
        print(self.id)
        # print(self.objects.get(id=self.id))
        print('DEBUG-5-models.py')

    class Meta:
        verbose_name = u'回覧板'
        verbose_name_plural = u'回覧板'

    def __unicode__(self):
        return self.title
