
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from celery.schedules import crontab
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-txh#u@-bw6ll(unih0@vro(#^7m875^t$-ga7^yf6k^dd2d%(0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd
    'debug_toolbar',
    'django_extensions',
    'rangefilter',

    'currency',
    'import_export',
    'accounts',
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'currency.middlewares.ResponseLogMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / '..' / 'static_content' / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testtestapp454545@gmail.com'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('login')

AUTH_USER_MODEL = 'accounts.User'

# TODO move to env
HTTP_SCHEMA = 'http'
DOMAIN = 'localhost:8000'

CELERY_BROKER_URL = 'amqp://localhost'
CELERY_BEAT_SCHEDULE = {
    'parse_privatbank': {
        'task': 'currency.tasks.parse_privatbank',
        'schedule': crontab(minute='*/2'),
    },
    'parse_monobank': {
        'task': 'currency.tasks.parse_monobank',
        'schedule': crontab(minute='*/2'),
    },
    'parse_vkurse': {
        'task': 'currency.tasks.parse_vkurse',
        'schedule': crontab(minute='*/2'),
    },
    'parse_oschadbank': {
        'task': 'currency.tasks.parse_oschadbank',
        'schedule': crontab(minute='*/2'),
    },
    'parse_finance_ua': {
        'task': 'currency.tasks.parse_finance_ua',
        'schedule': crontab(minute='*/2'),
    },
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
