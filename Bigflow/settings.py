"""
Django settings for Bigflow project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
from environs import Env
from Bigflow.Core import models as common
env = Env()
env.read_env()  # read .env file, if it exists
#SECRET_KEY = env('SECRET_KEY')
#Password_Key = env('Password_Key_for_encrypt')
try:
    Password_Key = env.str('Password_Key_for_encrypt')
except:
    common.logger.error([{"Password_Key_for_encrypt": "No name Password_Key_for_encrypt in env"}])
#DEBUG = env('DEBUG')
#SECRET_KEY = '3-b^6=oc54w-went7pzjb197ri2iu*p-n(rum13i-gshg@57#g'
try:
    SECRET_KEY = env.str('SECRET_KEY')
except:
    common.logger.error([{"SECRET_KEY": "No name SECRET_KEY in env"}])
# DEBUG = env.bool('DEBUG')
DEBUG = False
try:
    S3_BUCKET_NAME = env.str('S3_BUCKET_NAME')
except:
    common.logger.error([{"S3_BUCKET_NAME": "No name S3_BUCKET_NAME in env"}])
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
# This will be a password key for encrypt and decrypt datas(We may change key what ever we want)
#Password_Key = 'KVBank@Teynampet_head_ofc'
# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '3-b^6=oc54w-went7pzjb197ri2iu*p-n(rum13i-gshg@57#g'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

# ALLOWED_HOSTS = [
#     'vysfin-sit.ap-south-1.elasticbeanstalk.com',
#     'emc-vysfin-sit.kvbank.in'
# ]
try:
    ALLOWED_HOSTS = env.list("ALLOWED_HOST")
except:
    common.logger.error([{"ALLOWED_HOST": "No name ALLOWED_HOST in env"}])

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Bigflow.Core',
    'Bigflow.Master',
    'Bigflow.Transaction',
    'Bigflow.UserMgmt',
    'Bigflow.Purchase',
    'Bigflow.Service',
    'Bigflow.AP',
    'Bigflow.inward',
    'Bigflow.BOM',
    'rest_framework',
    'Bigflow.API',
    'rest_framework.authtoken',
    'Bigflow.Inventory',
    'Bigflow.Collection',
    'Bigflow.Sales',
    'Bigflow.Report',
    'Bigflow.ATMA',
    'Bigflow.FA',
    'Bigflow.BranchExp',
    'Bigflow.Proofing',
    'Bigflow.MEP',
    'Bigflow.StandardInstructions',
    'Bigflow.ServiceManagement',
    'Bigflow.Memo',
    'Bigflow.eClaim',
    'Bigflow.JV',
    'Bigflow.EBexpense',
    'Bigflow.JVWiseFin',
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

ROOT_URLCONF = 'Bigflow.urls'
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760 #10mb
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/Bigflow/Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'customer_tags': 'Bigflow.menuClass',

            }
        },
    },
]

WSGI_APPLICATION = 'Bigflow.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vsolvstab@gmail.com'
EMAIL_HOST_PASSWORD = 'stabchristmas_day'
EMAIL_PORT = 587

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
try:
    DB_ENGINE = env.str('DB_ENGINE')
except:
    common.logger.error([{"DB_ENGINE": "No name DB_ENGINE in env"}])
try:
    DB_NAME = env.str('DB_NAME')
except:
    common.logger.error([{"DB_NAME": "No name DB_NAME in env"}])
try:
    DB_NAME_1 = env.str('DB_NAME_1')
except:
    common.logger.error([{"DB_NAME_1": "No name DB_NAME_1 in env"}])
try:
    DB_USER = env.str('DB_USER')
except:
    common.logger.error([{"DB_USER": "No name DB_USER in env"}])
try:
    DB_PASSWORD = env.str('DB_PASSWORD')
except:
    common.logger.error([{"DB_PASSWORD": "No name DB_PASSWORD in env"}])
try:
    DB_HOST = env.str('DB_HOST')
except:
    common.logger.error([{"DB_HOST": "No name DB_HOST in env"}])
try:
    DB_PORT = env.str('DB_PORT')
except:
    common.logger.error([{"DB_PORT": "No name DB_PORT in env"}])
DATABASES = {
   'default': {
       'ENGINE': DB_ENGINE,
       'NAME': DB_NAME,
       'USER': DB_USER,
       'PASSWORD': DB_PASSWORD,
       'HOST': DB_HOST,
       'PORT': DB_PORT,
   },
    'eclaim_db': {
       'ENGINE': DB_ENGINE,
       'NAME': DB_NAME_1,
       'USER': DB_USER,
       'PASSWORD': DB_PASSWORD,
       'HOST': DB_HOST,
       'PORT': DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

import os
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)

LOGIN_URL = 'login'


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')


MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )

}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vsolvstab@gmail.com'
EMAIL_HOST_PASSWORD = 'stabchristmas_day'
EMAIL_PORT = 587



from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=90),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=90),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
}


# SESSION_COOKIE_AGE = env.int('SESSION_COOKIE_AGE') * 60
SESSION_COOKIE_AGE = 60*15
SESSION_SAVE_EVERY_REQUEST = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}