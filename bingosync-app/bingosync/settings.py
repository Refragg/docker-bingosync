"""
Django settings for bingosync project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

IS_PROD = False

from bingosync.secret_settings import SECRET_KEY, ADMINS, SERVER_EMAIL, DB_USER

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not IS_PROD

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

EMAIL_HOST = "localhost"
EMAIL_PORT = 25


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'crispy_forms',
    'url_tools',
    'bingosync'
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'bingosync.middleware.NotAuthenticatedMiddleware',
    'bingosync.middleware.InvalidRequestMiddleware',
)

ROOT_URLCONF = 'bingosync.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + "/templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'url_tools.context_processors.current_url',
            ],
        },
    },
]

WSGI_APPLICATION = 'bingosync.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bingosync',
        'USER': DB_USER,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Logging
# https://docs.djangoproject.com/en/1.8/topics/logging/
LOG_DIR_ROOT = os.path.join(BASE_DIR, "logs")
MAX_LOG_FILE_SIZE = 10 * (1024 ** 2)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '\u001b[1m{levelname:4.4} {module}.{funcName}:\u001b[0m {message}',
            'style': '{'
        },
        'verbose': {
            'format': '\u001b[1m{levelname:4.4} {asctime} {module}.{funcName}:\u001b[0m {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'info_log': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR_ROOT, 'info.log'),
            'mode': 'a',
            'maxBytes': MAX_LOG_FILE_SIZE,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'warn_log': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR_ROOT, 'warn.log'),
            'mode': 'a',
            'maxBytes': MAX_LOG_FILE_SIZE,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR_ROOT, 'error.log'),
            'mode': 'a',
            'maxBytes': MAX_LOG_FILE_SIZE,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'info_log', 'warn_log', 'error_log', 'mail_admins'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'bingosync': {
            'handlers': ['console', 'info_log', 'warn_log', 'error_log', 'mail_admins'],
            'level': 'INFO',
        },
    },
}


# base directory for data consumed in tests
TESTDATA_DIR = os.path.join(BASE_DIR, "testdata")

# base directory for data consumed in test_generator.py
GEN_TESTDATA_DIR = os.path.join(TESTDATA_DIR, "gen_output")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)

STATIC_ROOT = '/var/www/bingosync.com/static/'


INTERNAL_SOCKETS_URL = "127.0.0.1:8888"
PUBLIC_SOCKETS_URL = "sockets.bingosync.com"

if IS_PROD:
    SOCKETS_URL = "wss://" + PUBLIC_SOCKETS_URL
else:
    SOCKETS_URL = "ws://" + INTERNAL_SOCKETS_URL

# used for publishing events from django to tornado, so can always go across localhost
SOCKETS_PUBLISH_URL = "http://" + INTERNAL_SOCKETS_URL


# crispy forms confiuguration
CRISPY_TEMPLATE_PACK = 'bootstrap3'
