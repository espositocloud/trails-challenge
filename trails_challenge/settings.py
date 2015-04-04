"""
Django settings for trails_challenge project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jlz%=q&4glq2)fhvzlep=4tkgfkt=r3_5!oxvq(l-pu=tvm^r_'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False

#TEMPLATE_DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [ 'trailschallenge.ancona5.it', ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'challenge',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.middleware.cache.UpdateCacheMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'trails_challenge.urls'

WSGI_APPLICATION = 'trails_challenge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trails_challenge',
        'USER': 'trails_challenge',
        'PASSWORD': 'supertrails',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/trails_challenge/static'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_VERIFY_EXPIRATION': False,
}

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#        'LOCATION': '/tmp/uwsgi_cache',
#        'TIMEOUT': 10,
#    }
#}
#CACHE_MIDDLEWARE_SECONDS = 10
