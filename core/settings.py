"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from django.urls import reverse_lazy
from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
# reading .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# SECRET_KEY = env("SECRET_KEY")
SECRET_KEY = 'django-insecure-h&5)o*1qwd8)z(grg1ywfa6no&@f%1ftlnt9nqpo33q6ghbhvh'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-h&5)o*1qwd8)z(grg1ywfa6no&@f%1ftlnt9nqpo33q6ghbhvh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reservation',
    'account',
    'crispy_forms',
    "crispy_tailwind",
    'ckeditor',
    'django_filters',
    'phonenumber_field',
    'rosetta',
    'actions.apps.ActionsConfig',
    'reports',
    'django.contrib.humanize',
    'transport',
    'clients'
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = 'tailwind'
PHONENUMBER_DB_FORMAT = "E164"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default':env.db()
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ar'

DEFAULT_LANGUAGE = 'ar'
LANGUAGES = (
    ('ar', _('Arabic')),
    # ('en', _('English')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BOOKING_TIME_INTERVAL= 'nights'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

WHITENOISE_USE_FINDERS = True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


LOGIN_REDIRECT_URL = 'reservation:home'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('account:user_detail', args=[u.username]),
    'reservation.hotel': lambda u: reverse_lazy('reservation:hotel_detail', args=[u.slug]),
    'reservation.hotelpackage': lambda u: reverse_lazy('reservation:package_detail', args=[u.id]),
    'reservation.trip': lambda u: reverse_lazy('reservation:trip_detail', args=[u.id]),
    'reservation.tripbooking': lambda u: reverse_lazy('reservation:trip_booking_detail', args=[u.id]),
    'reservation.tripbookingprogram': lambda u: reverse_lazy('reservation:trip_booking_detail', args=[u.booking.id]),
    'reservation.additionalamount': lambda u: reverse_lazy('reservation:trip_booking_detail', args=[u.booking.id]),
    'reservation.booking': lambda u: reverse_lazy('reservation:booking_detail', args=[u.id]),
    'transport.bus': lambda u: reverse_lazy('transport:bus_detail', args=[u.id]),
    'reservation.client': lambda u: reverse_lazy('clients:client_detail', args=[u.id]),

}

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'basic',
    },
}
