# -*- coding: utf-8 -*-
# ==============================================================================
# Django settings for Voty project
# ==============================================================================
#Generated by 'django-admin startproject' using Django 3.0.2.
# full settings on https://docs.djangoproject.com/en/3.0/ref/settings/
#
# parameters (*default)
# ------------------------------------------------------------------------------

import os
import configparser

from django.utils.translation import ugettext_lazy as _

# ================================= HELPERS ====================================
def _strip(snippet):
  return snippet.partition('{% trans "')[2].partition('" %}')[0]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['UNSECURE_SECRET_KEY_VALUE']

# Retrieve initialization configuration, use raw parser i18n-texts
CUSTOM_DICT = configparser.RawConfigParser()
CUSTOM_DICT.optionxform=str
CUSTOM_DICT.read(os.path.join(BASE_DIR, "init.ini"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

      # locally
    "mysite.init_admin",
    "mysite.init_app",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
          os.path.join(BASE_DIR, "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST_VALUE']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER_VALUE']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD_VALUE']
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#EMAIL_HOST = CUSTOM_DICT.get("settings", "EMAIL_HOST_VALUE")
#EMAIL_HOST_USER = CUSTOM_DICT.get("settings", EMAIL_HOST_USER_VALUE)
#EMAIL_HOST_PASSWORD = CUSTOM_DICT.get("settings", "EMAIL_HOST_PASSWORD_VALUE")
#EMAIL_PORT = CUSTOM_DICT.get("settings", "EMAIL_PORT_VALUE")
#EMAIL_USE_TLS = CUSTOM_DICT.get("settings", "EMAIL_USE_TLS_VALUE")
#EMAIL_USE_SSL = CUSTOM_DICT.get("settings", "EMAIL_USE_SSL_VALUE")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER 
MAILER_EMAIL_BACKEND = EMAIL_BACKEND

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# to build language files, use 
# django-admin makemessages -l de -e html,txt,ini,py
# translate: https://localise.biz/free/poeditor
LOCALE_PATHS = (
  os.path.join( BASE_DIR, "locale"),
)

ACCOUNT_LANGUAGES = tuple([(x[0], _(_strip(x[1]))) for x in CUSTOM_DICT.items("alternative_language_list")])

LANGUAGES = ACCOUNT_LANGUAGES
LANGUAGE_CODE = CUSTOM_DICT.get("settings", "DEFAULT_LANGUAGE")
TIME_ZONE = CUSTOM_DICT.get("settings", "DEFAULT_TIMEZONE")
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (

  # Put strings here, like "/home/html/static" or "C:/www/django/static".
  # Always use forward slashes, even on Windows.
  # Don"t forget to use absolute paths, not relative paths.
  os.path.join( BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join( BASE_DIR, "public", "static")

ALLOWED_HOSTS = ['*']
X_FRAME_OPTIONS = '*'