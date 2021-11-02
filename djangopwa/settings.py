"""
Django settings for djangopwa project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'staticfiles/js', 'serviceworker.js')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = [
    'pwango.herokuapp.com/',
]

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'pwapp',
    'pwa',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangopwa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangopwa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




PWA_APP_NAME = 'Django PWA'
PWA_APP_THEME_COLOR = '#2196f3'
PWA_APP_BACKGROUND_COLOR = '#000000'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_ICONS = [
    {
        "src": "/static/images/icons/windows11/SmallTile.scale-100.png",
        "sizes": "71x71"
    }, {
        "src": "/static/images/icons/windows11/SmallTile.scale-125.png",
        "sizes": "89x89"
    }, {
        "src": "/static/images/icons/windows11/SmallTile.scale-150.png",
        "sizes": "107x107"
    }, {
        "src": "/static/images/icons/windows11/SmallTile.scale-200.png",
        "sizes": "142x142"
    }, {
        "src": "/static/images/icons/windows11/SmallTile.scale-400.png",
        "sizes": "284x284"
    }, {
        "src": "/static/images/icons/windows11/Square150x150Logo.scale-100.png",
        "sizes": "150x150"
    }, {
        "src": "/static/images/icons/windows11/Square150x150Logo.scale-125.png",
        "sizes": "188x188"
    }, {
        "src": "/static/images/icons/windows11/Square150x150Logo.scale-150.png",
        "sizes": "225x225"
    }, {
        "src": "/static/images/icons/windows11/Square150x150Logo.scale-200.png",
        "sizes": "300x300"
    }, {
        "src": "/static/images/icons/windows11/Square150x150Logo.scale-400.png",
        "sizes": "600x600"
    }, {
        "src": "/static/images/icons/windows11/Wide310x150Logo.scale-100.png",
        "sizes": "310x150"
    }, {
        "src": "/static/images/icons/windows11/Wide310x150Logo.scale-125.png",
        "sizes": "388x188"
    }, {
        "src": "/static/images/icons/windows11/Wide310x150Logo.scale-150.png",
        "sizes": "465x225"
    }, {
        "src": "/static/images/icons/windows11/Wide310x150Logo.scale-200.png",
        "sizes": "620x300"
    }, {
        "src": "/static/images/icons/windows11/Wide310x150Logo.scale-400.png",
        "sizes": "1240x600"
    }, {
        "src": "/static/images/icons/windows11/LargeTile.scale-100.png",
        "sizes": "310x310"
    }, {
        "src": "/static/images/icons/windows11/LargeTile.scale-125.png",
        "sizes": "388x388"
    }, {
        "src": "/static/images/icons/windows11/LargeTile.scale-150.png",
        "sizes": "465x465"
    }, {
        "src": "/static/images/icons/windows11/LargeTile.scale-200.png",
        "sizes": "620x620"
    }, {
        "src": "/static/images/icons/windows11/LargeTile.scale-400.png",
        "sizes": "1240x1240"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.scale-100.png",
        "sizes": "44x44"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.scale-125.png",
        "sizes": "55x55"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.scale-150.png",
        "sizes": "66x66"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.scale-200.png",
        "sizes": "88x88"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.scale-400.png",
        "sizes": "176x176"
    }, {
        "src": "/static/images/icons/windows11/StoreLogo.scale-100.png",
        "sizes": "50x50"
    }, {
        "src": "/static/images/icons/windows11/StoreLogo.scale-125.png",
        "sizes": "63x63"
    }, {
        "src": "/static/images/icons/windows11/StoreLogo.scale-150.png",
        "sizes": "75x75"
    }, {
        "src": "/static/images/icons/windows11/StoreLogo.scale-200.png",
        "sizes": "100x100"
    }, {
        "src": "/static/images/icons/windows11/StoreLogo.scale-400.png",
        "sizes": "200x200"
    }, {
        "src": "/static/images/icons/windows11/SplashScreen.scale-100.png",
        "sizes": "620x300"
    }, {
        "src": "/static/images/icons/windows11/SplashScreen.scale-125.png",
        "sizes": "775x375"
    }, {
        "src": "/static/images/icons/windows11/SplashScreen.scale-150.png",
        "sizes": "930x450"
    }, {
        "src": "/static/images/icons/windows11/SplashScreen.scale-200.png",
        "sizes": "1240x600"
    }, {
        "src": "/static/images/icons/windows11/SplashScreen.scale-400.png",
        "sizes": "2480x1200"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-16.png",
        "sizes": "16x16"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-20.png",
        "sizes": "20x20"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-24.png",
        "sizes": "24x24"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-30.png",
        "sizes": "30x30"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-32.png",
        "sizes": "32x32"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-36.png",
        "sizes": "36x36"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-40.png",
        "sizes": "40x40"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-44.png",
        "sizes": "44x44"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-48.png",
        "sizes": "48x48"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-60.png",
        "sizes": "60x60"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-64.png",
        "sizes": "64x64"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-72.png",
        "sizes": "72x72"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-80.png",
        "sizes": "80x80"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-96.png",
        "sizes": "96x96"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.targetsize-256.png",
        "sizes": "256x256"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-16.png",
        "sizes": "16x16"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-20.png",
        "sizes": "20x20"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-24.png",
        "sizes": "24x24"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-30.png",
        "sizes": "30x30"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-32.png",
        "sizes": "32x32"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-36.png",
        "sizes": "36x36"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-40.png",
        "sizes": "40x40"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-44.png",
        "sizes": "44x44"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-48.png",
        "sizes": "48x48"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-60.png",
        "sizes": "60x60"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-64.png",
        "sizes": "64x64"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-72.png",
        "sizes": "72x72"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-80.png",
        "sizes": "80x80"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-96.png",
        "sizes": "96x96"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-unplated_targetsize-256.png",
        "sizes": "256x256"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-16.png",
        "sizes": "16x16"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-20.png",
        "sizes": "20x20"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-24.png",
        "sizes": "24x24"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-30.png",
        "sizes": "30x30"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-32.png",
        "sizes": "32x32"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-36.png",
        "sizes": "36x36"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-40.png",
        "sizes": "40x40"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-44.png",
        "sizes": "44x44"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-48.png",
        "sizes": "48x48"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-60.png",
        "sizes": "60x60"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-64.png",
        "sizes": "64x64"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-72.png",
        "sizes": "72x72"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-80.png",
        "sizes": "80x80"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-96.png",
        "sizes": "96x96"
    }, {
        "src": "/static/images/icons/windows11/Square44x44Logo.altform-lightunplated_targetsize-256.png",
        "sizes": "256x256"
    }, {
        "src": "/static/images/icons/android-launchericon-512-512.png",
        "sizes": "512x512"
    }, {
        "src": "/static/images/icons/android-launchericon-192-192.png",
        "sizes": "192x192"
    }, {
        "src": "/static/images/icons/android-launchericon-144-144.png",
        "sizes": "144x144"
    }, {
        "src": "/static/images/icons/android-launchericon-96-96.png",
        "sizes": "96x96"
    }, {
        "src": "/static/images/icons/android-launchericon-72-72.png",
        "sizes": "72x72"
    }, {
        "src": "/static/images/icons/android-launchericon-48-48.png",
        "sizes": "48x48"
    }, {
        "src": "/static/images/icons/ios/16.png",
        "sizes": "16x16"
    }, {
        "src": "/static/images/icons/ios/20.png",
        "sizes": "20x20"
    }, {
        "src": "/static/images/icons/ios/29.png",
        "sizes": "29x29"
    }, {
        "src": "/static/images/icons/ios/32.png",
        "sizes": "32x32"
    }, {
        "src": "/static/images/icons/ios/40.png",
        "sizes": "40x40"
    }, {
        "src": "/static/images/icons/ios/50.png",
        "sizes": "50x50"
    }, {
        "src": "/static/images/icons/ios/57.png",
        "sizes": "57x57"
    }, {
        "src": "/static/images/icons/ios/58.png",
        "sizes": "58x58"
    }, {
        "src": "/static/images/icons/ios/60.png",
        "sizes": "60x60"
    }, {
        "src": "/static/images/icons/ios/64.png",
        "sizes": "64x64"
    }, {
        "src": "/static/images/icons/ios/72.png",
        "sizes": "72x72"
    }, {
        "src": "/static/images/icons/ios/76.png",
        "sizes": "76x76"
    }, {
        "src": "/static/images/icons/ios/80.png",
        "sizes": "80x80"
    }, {
        "src": "/static/images/icons/ios/87.png",
        "sizes": "87x87"
    }, {
        "src": "/static/images/icons/ios/100.png",
        "sizes": "100x100"
    }, {
        "src": "/static/images/icons/ios/114.png",
        "sizes": "114x114"
    }, {
        "src": "/static/images/icons/ios/120.png",
        "sizes": "120x120"
    }, {
        "src": "/static/images/icons/ios/128.png",
        "sizes": "128x128"
    }, {
        "src": "/static/images/icons/ios/144.png",
        "sizes": "144x144"
    }, {
        "src": "/static/images/icons/ios/152.png",
        "sizes": "152x152"
    }, {
        "src": "/static/images/icons/ios/167.png",
        "sizes": "167x167"
    }, {
        "src": "/static/images/icons/ios/180.png",
        "sizes": "180x180"
    }, {
        "src": "/static/images/icons/ios/192.png",
        "sizes": "192x192"
    }, {
        "src": "/static/images/icons/ios/256.png",
        "sizes": "256x256"
    }, {
        "src": "/static/images/icons/ios/512.png",
        "sizes": "512x512"
    }, {
        "src": "/static/images/icons/ios/1024.png",
        "sizes": "1024x1024"
    }
  ]

DEBUG_PROPAGATE_EXCEPTIONS = True
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

# Activate Django-Heroku.
django_heroku.settings(locals())

