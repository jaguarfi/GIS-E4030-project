"""
Django settings for mapservice project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-%rrm!d5i7z82co0w-#788dz=3m4db6&9@mo2=c9xwpdvy%j!^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
	'mapapp',
	'leaflet',
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

ROOT_URLCONF = 'mapservice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
         os.path.join(BASE_DIR, 'mapapp/templates/'),
         os.path.join(BASE_DIR, 'mapservice/templates/'),
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

WSGI_APPLICATION = 'mapservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

#--done later, conditionally


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


#Fix for each system separately?
import os

#check username to determine system and fix parameters conditionally:
if os.environ['USERNAME'] == 'juhani':
    DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'GIS_DB1',
        'USER': 'postgres',
        'PASSWORD': 'ApinaVapina',
        'HOST': 'localhost',
    }
    }
    GDAL_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\gdal204.dll'
        
elif os.environ['USERNAME'] == 'Jhosea':
    DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'GIS_DB',
        'USER': 'postgres',
        'PASSWORD': 'admin#2019#aalto',
    }
    }
elif os.environ['USERNAME'] == 'Tekla':
    DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgis_25_sample',
        'USER': 'postgres',
        'PASSWORD': 'ApinaVapina',
        'HOST': 'localhost',
    }
    }
    GDAL_LIBRARY_PATH = 'C:\\OSGeo4W64\\bin\\gdal204.dll'
elif os.environ['USERNAME'] == 'Bijay Karki':
    DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'GIS_DB1',
        'USER': 'postgres',
        'PASSWORD': 'karki',
        'HOST': 'localhost',
        'PORT' : '5433',
    }
    }
    GDAL_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\gdal204.dll'
else:
    raise ValueError("If you are seeing this go to settings.py and define custom parameters to be used in your environment, at least for your PostGIS database, see lines 125-170 for examples")




#Added a textual logger for easier tracing
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'handlers': {
    'file': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
    },
},
'loggers': {
    'django': {
        'handlers': ['file',],
        'level': 'DEBUG',
        'propagate': True,
    },
},
}


#Settings for Django-Leaflet  60.186829   24.821367
LEAFLET_CONFIG = {
    #'SPATIAL_EXTENT': (), not sure how to fill params - needs 4. long/lats?
    'DEFAULT_CENTER': (60.18695, 24.820), #coords for rougly tik-talo, one of the two buildings
    'DEFAULT_ZOOM': 18,
    'MIN_ZOOM': 10,
    'MAX_ZOOM': 19,
    'SCALE': 'metric',
}

