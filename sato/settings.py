#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
Django settings for sato project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

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
    'django_cron',
    'django_extensions',
    'grappelli',
    'filebrowser',
    'easy_thumbnails',
    'filer',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',

    # myapps
    'lib',
    'news',
    'home',
    'activity',
    'emergency',
    'formats',
    'board',
    'about',
    'security',
    'lab',
    'todo',
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
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', 'HorizontalRule', '-', 'BidiLtr', 'BidiRtl', 'Language', '-', 'Table', 'Link', 'Unlink', 'Image', 'Slideshow', 'SpecialChar', 'HorizontalRule', 'PageBreak', 'Smiley', 'wenzgmap', 'Iframe'],
                    ['Undo', 'Redo', '-', 'Styles', 'Format', 'Font', 'FontSize', 'lineheight', '-', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'TextColor', 'BGColor',]
        ],
        'extraPlugins': 'quicktable,slideshow,wenzgmap,attach,uploadimage,lineheight,filetools,stylesheetparser,imagerotate,tableresize,image2,autogrow,colordialog,imagepaste,autoembed',
        'allowedContent': True,
        # 'height': 400,
        # 'width': 00,
    },
    'simple': {
        'skin': 'office2013',
        'toolbar': [['Save', 'NewPage', 'Templates', 'Cut', 'Copy', 'Paste', 'PasteText', '-', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', '-', 'Link', 'Unlink', 'SpecialChar', 'PageBreak', 'Smiley', '-', 'Find', 'Replace', '-', 'SelectAll', '-', 'Source', 'Print', 'Maximize', ],
                    ['Undo', 'Redo', '-', 'Styles', 'Format', 'Font', 'FontSize', 'lineheight', '-', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'TextColor', 'BGColor',]
        ],
        'extraPlugins': 'slideshow,attach,lineheight,autogrow,colordialog,autoembed',
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'satodb.sqlite3'),
    }
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

try:
    from local_settings import *
except ImportError:
    pass
