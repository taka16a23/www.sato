#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import forms
from django.db.models.signals import post_save
from django.core.files import File

from core.models import DisplayableModel
from core.managers import DisplayableManager

# import uuid
import os
import datetime
from sato import settings
import subprocess as sbp
# import hashlib
import tempfile
import contextlib
import shutil


# def get_hash_name(fobj):
#     r"""SUMMARY

#     get_hash_name(fobj)

#     @Arguments:
#     - `fobj`:

#     @Return:

#     @Error:
#     """
#     fobj.seek(0)
#     md5 = hashlib.md5()
#     if fobj.multiple_chunks():
#         md5.update(fobj.chunks())
#     else:
#         md5.update(fobj.read())
#     fobj.seek(0)
#     return md5.hexdigest()


# # TODO: (Atami) [2016/02/17]
# # can't remove
# def get_file_path(instance, filename):
#     return os.path.join('boards', get_hash_name(instance.file) + '.pdf')

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
        verbose_name = u'回覧物(PDF)'
        verbose_name_plural = u'回覧物(PDF)'

    def __unicode__(self):
        return self.title



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# models.py ends here
