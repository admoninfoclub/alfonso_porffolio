# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import django.contrib.auth
from pathlib import Path

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
django.contrib.auth.LOGIN_URL = '/'
import dj_database_url  #obligatoria para RENDER

BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '4#7qom+fo@!0a@v@%u29rqu@hq&m1#oev9dk#4o(nb006cs_3^'
#DEBUG = True #ESTO ES PARA DESARROLLO Y False para producción
DEBUG = False #producción para RENDER
#ALLOWED_HOSTS = []   #Permite conexión desde cualquier host
ALLOWED_HOSTS = ['https://alfonso-portfolio.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appportfolio',
    'allauth',
]
'''
    'allauth.account',
    'allauth.socialaccount',
	'allauth.socialaccount.providers.facebook', # if you need FB api
	'allauth.socialaccount.providers.google',
	'allauth.socialaccount.providers.instagram',
	'allauth.socialaccount.providers.linkedin',
	'allauth.socialaccount.providers.xing',
'''

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'pportfolio.urls'
WSGI_APPLICATION = 'pportfolio.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        # este directorio no puede estar vacío es donde busca las plantillas hay que incluirlo
        # este concretamente utiliza el directorio templates del proyecto
        # 'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [  # procesadores de contexto
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


'''
version de postgresql_psycopg2 2.7.5
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'bdportfolio', #siempre en minúsculas para heroku
		'USER': 'postgres', #este usuario es por defecto
		'PASSWORD': '', #al desplegarlo en heroku debe llevar clave
		'HOST': 'localhost', #lo asume heroku por defecto y nuestra máquina
		'PORT': '5432',  #lo asume heroku por defecto y nuestra máquina
	}
}
'''
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
SITE_ID = 1
SITE_NAME = "Portfolio"
#SITE_URL = "http://127.0.0.1:8000/"
LANGUAGE_CODE = 'es-ES'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'djblets.siteconfig.context_processors.siteconfig',
    'djblets.util.context_processors.settingsVars',
    'djblets.util.context_processors.siteRoot',
    'djblets.util.context_processors.ajaxSerial',
    'djblets.util.context_processors.mediaSerial',
	'django.template.context_processors.request',
)

#la parte estática es obligatoria para Heroku y para nuestra máquina
STATIC_URL = '/static/'    #js, css3, ..
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'  #videos, imágenes
STATIC_ROOT= os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  segun render

# declara la ruta donde se enlazará el contenido estático
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
	('css', os.path.join(STATIC_ROOT, 'css')),
	('js', os.path.join(STATIC_ROOT, 'js')),
	('images', os.path.join(STATIC_ROOT, 'images')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
)

DEFAULT_AUTO_FIELD ="django.db.models.BigAutoField"

#correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587 
EMAIL_HOST_USER = 'infoclub3000@gmail.com'# emisor 
EMAIL_HOST_PASSWORD = 'aaaaaaaaaa'
EMAIL_USE_TLS = True  #seguridad de gmail
#EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

