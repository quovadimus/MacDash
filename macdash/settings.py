"""
Django settings for macdash project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

#################################################
#               POSTGRES SETTINGS               #
#################################################
USE_POSTGRES = True

POSTGRES_USERNAME = os.environ.get('POSTGRES_USERNAME', '')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
POSTGRES_DB_NAME = os.environ.get('POSTGRES_DB_NAME', 'macdash')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')


#################################################
#              END OF CUSTOM SETTINGS           #
#################################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mct$y5o9&m+uq&n45f4^$=#iw&1ploor&3nlyj&&s0!go(cxkq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'


# Application definition

INSTALLED_APPS = [
    'dash.apps.DashConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'settings_context_processor',
]

if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')

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

ROOT_URLCONF = 'macdash.urls'

# Add static folder to STATIC_DIRS
# STATICFILES_DIRS = [
# os.path.join(BASE_DIR, "static"),
# ]

# Add templates to DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  #modify this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settings_context_processor.context_processors.settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'macdash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if USE_POSTGRES:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': POSTGRES_DB_NAME,
            'USER': POSTGRES_USERNAME,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': POSTGRES_HOST,
            'PORT': POSTGRES_PORT,   
        }
    }
else:   
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TEMPLATE_VISIBLE_SETTINGS = []

try:
    from custom_settings import *

    if 'MACDASH_BRANDING' in globals():
        TEMPLATE_VISIBLE_SETTINGS.append('MACDASH_BRANDING')
except ImportError:
    pass
