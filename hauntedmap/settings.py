"""
Django settings for hauntedmap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
import django_facebook
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@hvs+xre9gh$#xxg-jzf_)j)(pqk8zffb@qe675)tz9@qy_8@m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',
    'website',
    'external_data',
    'django_facebook',
    'django_jenkins'
    #'gunicorn'
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',    # This middleware must be first on the list
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hauntedmap.urls'

WSGI_APPLICATION = 'hauntedmap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'hauntedmap',
        'USER': 'appUser',
        'HOST': '54.243.238.190',
        'PASSWORD': 'FulGrain123$'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#
# #Redis Session Cache
# SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_DB = 0
# SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'
# SESSION_REDIS_PASSWORD = 'ci[BRr=rCP4_;F)'
#
# #BackEnd Cache
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '/var/run/redis/redis.sock',
#         'OPTIONS': {
#               'DB': 0,
#             'PASSWORD': 'ci[BRr=rCP4_;F)',
#             }
#     },
#     }

#Facebook App Secure Info
FACEBOOK_APP_ID = '275585332592670'
FACEBOOK_APP_SECRET = 'a9e1f9fc3b1f22bf42c800673e7abffb'

#Template Context Processors for FaceBook Integration

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
 "django_facebook.context_processors.facebook",)

#Authentication Backend
AUTHENTICATION_BACKENDS = (
    'django_facebook.auth_backends.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Custom User Model
AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'

# Custom Profile Model
AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'


#Logging
LOGGING_CONFIG = 'logging.config.dictConfig'



