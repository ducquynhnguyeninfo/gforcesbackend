"""
Django settings for vehicle_order_manager project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import urllib
from pathlib import Path
from os import path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_-5h8k*@cq1drcjfg2^l*=bt2o8zsfv5jhr6o_4jvos&48&(ar'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'localhost:4200']

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost',
    'http://localhost:8000',
    'http://localhost:4200',
)

# Application definition

INSTALLED_APPS = [
    'order_manager.apps.OrderManagerConfig',
    'rest_framework',
    # CORS
    'corsheaders',
    'querybuilder',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vehicle_order_manager.urls'

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

WSGI_APPLICATION = 'vehicle_order_manager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

db_usrname = "superadmin"
db_usrpwd = "12345678x@X"
db_cluster_name = "cluster0-gforces"
db_name = "gforce_vehicle_order_manager"

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    # 'default' : {
    #     "ENGINE":"djongo",
    #     "CLIENT": {
    #         "host": f"mongodb+srv://{db_usrname}:{db_usrpwd}@{db_cluster_name}.mongodb.net/?retryWrites=true&w=majority",
    #         "username": "superadmin",
    #         "password": f"{db_usrpwd}",
    #         "name": f"{db_name}",
    #         "authMechanism": "SCRAM-SHA-1",
    #     },
    # }
    #
    'default': {
        "ENGINE": "djongo",
        "NAME": "gforce_vehicle_order_manager-jgycy",
        "CLIENT": {
            "host": "mongodb+srv://superadmin:" + urllib.parse.quote_plus("12345678x") + "@Cluster0-gforces.pw4fq.mongodb.net/gforces_vehicle_manager?retryWrites=true&w=majority",
            "username": "superadmin",
            "password": "12345678x",
            # "name": "gforce_vehicle_order_manager-jgycy",
            "authMechanism": "SCRAM-SHA-1",
        },

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# APPEND_SLASH=False