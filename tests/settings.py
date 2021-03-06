# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import os
import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "2vvq2+^y4+trbuk$n%^6aa7%mr3c5lux_a0=unya_(-^o52%@&"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

AUTH_USER_MODEL = "gjwt_auth.User"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    
    "djoser",
    "graphene_django",

    "gjwt_auth",
]

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

if django.VERSION >= (1, 10):
    MIDDLEWARE = MIDDLEWARE_CLASSES

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


GRAPHENE = {
    'SCHEMA': 'tests.graphql_schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

DOMAIN = os.environ.get('DJANGO_DJOSER_DOMAIN', 'localhost:3000')
SITE_NAME = os.environ.get('DJANGO_DJOSER_SITE_NAME', 'my site')

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '?action=set-new-password&uid={uid}&token={token}',
    'ACTIVATION_URL': 'activate?uid={uid}&token={token}',
    'SEND_ACTIVATION_EMAIL': True,
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',
                'django.template.context_processors.static',
            ],

            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]
