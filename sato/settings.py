#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for sato project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/

setup memo
$ apt-get install mysql-server mysql-client libmysqlclient-dev
$ pip install mysql-python
$ mysql -u root -p
Enret password:
mysql> CREATE DATABASE sato DEFAULT CHARACTER SET utf8;
Query OK, 1 row affected (0.00 sec)
mysql> exit

"""
import os
import socket

from django.contrib import admin
from adminplus.sites import AdminSitePlus


class SatoAdminSite(AdminSitePlus):
    # Text to put at the end of each page's <title>.
    # site_title = u'里自治会'

    # Text to put in each page's <h1>.
    # site_header = u'里自治会ホームページ コントロールパネル'
    # site_title = u'里自治会'
    site_header = u'里自治会 ホームページ'
    index_title = u'コントロールパネル'
    # index_template = 'base/admin/index.html'
    # Text to put at the top of the admin index page.
    # index_title = u'里自治会ホームページ コントロールパネル'

admin.site = SatoAdminSite()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = '/var/www'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e#=uh+oj=vsk(az33dfjl%@=y7=4dekkjj^hubdha@4qimak5)'

# SECURITY WARNING: don't run with debug turned on in production!
if socket.gethostname() in ('ki', ):
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (('Atami', 'takahiroatsumi0517@gmail.com'), )


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'captcha',
    'django_extensions',
    'grappelli',
    'filebrowser',
    'easy_thumbnails',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'adminsortable2',
    'colorfield',
    'adminplus',
    'filer',

    # myapps
    'base',
    'home',
    'formats',
    'publish',
    'about',
    'security',
    'lab',
]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'office2013',
        # 'skin': 'kama',
        # 'skin': 'moonocolor',
        # 'skin': 'flat',
        # 'skin': 'moono-dark',
        # 'skin': 'moono_blue',
        # 'toolbar': 'full',
        'toolbar': [['Save', 'NewPage', 'Templates', '-', 'Find', 'Replace', '-', 'SelectAll', '-', 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField',  '-', 'Source', 'Blockquote', 'Anchor', 'CreateDiv', '-', 'Print', 'Preview', 'Maximize', ],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'HorizontalRule', '-', 'BidiLtr', 'BidiRtl', 'Language', '-', 'Table', 'Link', 'Unlink', 'Image', 'Slideshow', 'SpecialChar', 'HorizontalRule', 'PageBreak', 'Smiley', 'wenzgmap', 'Iframe', 'Timestamp'],
                    ['Undo', 'Redo', '-', 'Styles', 'Format', 'Font', 'FontSize', 'lineheight', '-', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'TextColor', 'BGColor']
        ],
        'extraPlugins': 'quicktable,slideshow,wenzgmap,attach,uploadimage,lineheight,filetools,stylesheetparser,imagerotate,tableresize,image2,autogrow,colordialog,imagepaste,autoembed,timestamp',
        'allowedContent': True,
        # 'height': 400,
        # 'width': 750,
    },
    'activity': {
        'skin': 'office2013',
        # 'skin': 'kama',
        # 'skin': 'moonocolor',
        # 'skin': 'flat',
        # 'skin': 'moono-dark',
        # 'skin': 'moono_blue',
        # 'toolbar': 'full',
        'toolbar': [['Save', 'NewPage', 'Templates', '-', 'Find', 'Replace', '-', 'SelectAll', '-', 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField',  '-', 'Source', 'Blockquote', 'Anchor', 'CreateDiv', '-', 'Print', 'Preview', 'Maximize', ],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'HorizontalRule', '-', 'BidiLtr', 'BidiRtl', 'Language', '-', 'Table', 'Link', 'Unlink', 'Image', 'Slideshow', 'SpecialChar', 'HorizontalRule', 'PageBreak', 'Smiley', 'wenzgmap', 'Iframe', 'Timestamp'],
                    ['Undo', 'Redo', '-', 'Styles', 'Format', 'Font', 'FontSize', 'lineheight', '-', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'TextColor', 'BGColor', 'timestamp']
        ],
        'extraPlugins': 'quicktable,slideshow,wenzgmap,attach,uploadimage,lineheight,filetools,stylesheetparser,imagerotate,tableresize,image2,autogrow,colordialog,imagepaste,autoembed,timestamp',
        'allowedContent': True,
        # 'height': 400,
        'width': 750,
    },
    'simple': {
        'skin': 'office2013',
        'toolbar': [['Save', 'NewPage', 'Templates', 'Cut', 'Copy', 'Paste', 'PasteText', '-', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', '-', 'Link', 'Unlink', 'SpecialChar', 'PageBreak', 'Smiley', '-', 'Find', 'Replace', '-', 'SelectAll', '-', 'Source', 'Print', 'Maximize', 'Timestamp'],
                    ['Undo', 'Redo', '-', 'Styles', 'Format', 'Font', 'FontSize', 'lineheight', '-', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'TextColor', 'BGColor', 'timestamp']
        ],
        'extraPlugins': 'slideshow,attach,lineheight,autogrow,colordialog,autoembed,timestamp',
        'allowedContent': True,
        'height': 100,
    },
}


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

ROOT_URLCONF = 'sato.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # 'templates',
                 '/var/www/sato/templates',
                 '/var/www/sato/formats/templates',
                 '/var/www/sato/about/templates',
                 '/var/www/sato/home/templates',
                 '/var/www/sato/activity/templates',
                 '/var/www/sato/news/templates',
                 '/var/www/sato/security/templates',
                 '/var/www/sato/base/templates',
                 # 'secportal/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static', # for {{ STATIC_URL }}
            ],
        },
    },
]

WSGI_APPLICATION = 'sato.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sato',
        'USER': 'root',
        'PASSWORD': 'toor',
        'HOST': '',
        'PORT': '',
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(DATA_DIR, 'static')
STATIC_URL = '/static/'
# STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, "static"),
# )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
MEDIA_URL = '/media/'

# FILEBROWSER_DIRECTORY = os.path.join(MEDIA_ROOT, 'uploads')
# FILEBROWSER_VERSIONS_BASEDIR = MEDIA_ROOT

THUMBNAIL_HIGH_RESOLUTION = True

### Email
#
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'satotanakami@gmail.com'
EMAIL_HOST_PASSWORD = 'Mochihi.'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


try:
    from local_settings import *
except ImportError:
    pass
