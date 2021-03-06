"""
Django settings for Jan18 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#base dir is the root of the project 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l6%1qke=&v!+r4ism2r2-h2a6)5=3kj4j_ta+esmpaqovm-i8v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yourgmail@gmail.com' 
EMAIL_HOST_PASSWORD = 'yourpassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

'''
If using gmail, you will need to unlock Captcha to
enable Django to send for you:
https://accounts.google.com/displayunlockcaptcha
'''
#domains allowed 

# Application definition
#an app has to be installed

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'newsletter',
    

    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Jan18.urls'
#How django knows what urls to go through

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'Jan18.wsgi.application'
#configuration folder

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#database settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
#language codes

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
#css java script  n images
#they dont change

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',  
]
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")


CRISPY_TEMPLATE_PACK= 'bootstrap3'

#Django reg redux settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN =True
SITE_ID = 1 
LOGIN_REDIRECT_URL = '/'