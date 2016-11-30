"""
Django settings for medik project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h_u5cy9#afq4np8efvcg$*@!!9t9$ch%u89r)+tsi3#7fi7rat'

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
	'django.contrib.sites',
    'django.contrib.flatpages',
	'django.contrib.comments',
	'easy_thumbnails',
	'taggit',
	'precise_bbcode',
	'main',
    'author',
    'news',
    'contacts',
    'reportlab'
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = "main"
SITE_ID = 1
THUMBNAIL_BASEDIR = "thumbnails"
LOGIN_URL = "login"
LOGOUT_URL = "logout"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'medik.urls'

WSGI_APPLICATION = 'medik.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/medik_db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
STATIC_URL = '/static/'
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Omsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
