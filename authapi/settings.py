from pathlib import Path
from os import getenv, path 
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#load env
env_path = path.join(BASE_DIR, '.env')
if  path.isfile(env_path):
    load_dotenv(dotenv_path=env_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DJANGO_DEBUG", "False") == "True"

ALLOWED_HOSTS = getenv("DJANGO_HOSTS", "localhost,127.0.0.1").split(',')

# Application definition
INSTALLED_APPS = [
    "jazzmin",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "djoser",

    "users"
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

ROOT_URLCONF = 'authapi.urls'

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

WSGI_APPLICATION = 'authapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv("DB_NAME", 'postgres'),
        'USER': getenv("DB_USER", 'postgres'),
        'PASSWORD': getenv("DB_PASSWORD", 'mysecretpassword'),
        'HOST': getenv("DB_HOST", "localhost"),
        'PORT': getenv("DB_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

# rest framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":[
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    'CREATE_SESSION_ON_LOGIN': True,
    "SEND_ACTIVATION_EMAIL": True,
    "TOKEN_MODEL": None,
}

#simple jwt settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = path.join(BASE_DIR, 'public')

MEDIA_URL = "media/"
MEDIA_ROOT = path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User"

JAZZMIN_SETTINGS = {
    "site_title": "Authapi",
    "site_header": "Authapi",
    "site_brand": "Auth api"
}

LIARA_ENDPOINT    = getenv("LIARA_ENDPOINT")
LIARA_BUCKET_NAME = getenv("LIARA_BUCKET_NAME")
LIARA_ACCESS_KEY  = getenv("LIARA_ACCESS_KEY")
LIARA_SECRET_KEY  = getenv("LIARA_SECRET_KEY")

AWS_ACCESS_KEY_ID       = LIARA_ACCESS_KEY
AWS_SECRET_ACCESS_KEY   = LIARA_SECRET_KEY
AWS_STORAGE_BUCKET_NAME = LIARA_BUCKET_NAME
AWS_S3_ENDPOINT_URL     = LIARA_ENDPOINT
AWS_S3_REGION_NAME      = 'us-east-1'

STORAGES = {
  "default": {
      "BACKEND": "storages.backends.s3.S3Storage",
  },
  "staticfiles": {
      "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
  },
}