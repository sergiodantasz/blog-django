"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from os import getenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.parent / 'data' / 'web'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', 'CHANGE')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(getenv('DEBUG', 0)))

ALLOWED_HOSTS = [
    host for host in getenv('ALLOWED_HOSTS', '').split(',')
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps
    'blog',
    'setup',

    # Django Summernote
    'django_summernote',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
                'setup.context_processors.setup'
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': getenv('DB_ENGINE', 'CHANGE'),
        'NAME': getenv('POSTGRES_DB', 'CHANGE'),
        'USER': getenv('POSTGRES_USER', 'CHANGE'),
        'PASSWORD': getenv('POSTGRES_PASSWORD', 'CHANGE'),
        'HOST': getenv('POSTGRES_HOST', 'CHANGE'),
        'PORT': getenv('POSTGRES_PORT', 'CHANGE'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = DATA_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = DATA_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SUMMERNOTE_CONFIG = {
    'summernote': {
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'clear']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph', 'hr']],
            ['table', ['table']],
            ['insert', ['link', 'picture']],
            ['view', ['fullscreen', 'codeview', 'undo', 'redo']]
        ],
        'codemirror': {
            'mode': 'htmlmixed',
            'lineNumbers': 'true',
            'theme': 'dracula',
            'lineWrapping': 'true'
        }
    },
    'css': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/theme/dracula.min.css',
    ),
    'attachment_filesize_limit': 30 * 1024 * 1024,
    'attachment_model': 'blog.PostAttachment'
}
