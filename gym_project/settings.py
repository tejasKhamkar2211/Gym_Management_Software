"""
Django settings for gym_project project.
"""

from pathlib import Path
import os

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = 'django-insecure-9u-iba7=*g40o7#rsnh5l1b7(dnmovf0el2$w4y9@r#mjha1ip'
DEBUG = True
ALLOWED_HOSTS = ['*']


# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gym_app',
]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'gym_project.urls'


# TEMPLATES
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


WSGI_APPLICATION = 'gym_project.wsgi.application'


# ==========================
# DATABASE CONFIGURATION
# ==========================

ENV = os.environ.get("ENV")

if ENV == "ci":
    # ✅ Jenkins / CI uses SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # ✅ Local / Production uses MySQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'final_gym_db',
            'USER': 'root',
            'PASSWORD': 'Ydl@123',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }


# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# STATIC FILES
STATIC_URL = 'static/'


# DEFAULT PRIMARY KEY FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
