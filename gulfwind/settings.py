from pathlib import Path

from . import secrets

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [
        '*.gulfwind.ru',
        'gulfwind.ru',
        'localhost',
        '127.0.0.1',
        '0.0.0.0',
        '127.0.0.0',
    ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'crispy_forms',
    'easy_thumbnails',
    'image_cropping',

    'core',
    'authentication',
    'profiles',
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

ROOT_URLCONF = 'gulfwind.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'gulfwind.wsgi.application'

POSTGRES = secrets.POSTGRES

if not POSTGRES:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': secrets.DB_NAME,
            'USER': secrets.DB_USER,
            'PASSWORD': secrets.DB_USER_PASSWORD,
            'HOST': secrets.DB_HOST,
            'PORT': secrets.DB_PORT,
        }
    }

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

from easy_thumbnails.conf import Settings as thumbnail_settings

THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800

SITE_ID = 1

FIRST_DAY_OF_WEEK = 1

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = secrets.EMAIL_HOST

EMAIL_PORT = secrets.EMAIL_PORT

EMAIL_HOST_USER = secrets.EMAIL_HOST_USER

EMAIL_HOST_PASSWORD = 'ScX1548850'

EMAIL_USE_TLS = secrets.EMAIL_USE_TLS

EMAIL_USE_SSL = secrets.EMAIL_USE_SSL

SERVER_EMAIL = EMAIL_HOST_USER

DEFAULT_FROM_EMAIL = f'Электронный рапорт <{EMAIL_HOST_USER}>'

ADMINS = secrets.ADMINS

MANAGERS = secrets.MANAGERS

EMAIL_SUBJECT_PREFIX = '[Галфвинд]'

EMAIL_USE_LOCALTIME = True

AUTH_USER_MODEL = 'authentication.User'

CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure' # TODO: override this

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'

ACCOUNT_USERNAME_REQUIRED = True

SOCIALACCOUNT_AUTO_SIGNUP = False
