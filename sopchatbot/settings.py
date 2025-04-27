from pathlib import Path
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# OpenAI Client Initialization
if 'collectstatic' not in sys.argv:
    openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add media file support
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
DEBUG = True
ALLOWED_HOSTS = ['sopchatbot.onrender.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "sop",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Ensure Whitenoise is included here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sopchatbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "sop/templates")],  # Ensures Django can find the templates
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

WSGI_APPLICATION = 'sopchatbot.wsgi.application'

# Database Configuration
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}

# Password Validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files (CSS, JavaScript, Images)
STATIC_URL = "/static/"  # URL to access static files in the browser
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # Directory for collectstatic (production)
# WhiteNoise Storage (used for serving static files in production)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Additional directory for static files during development
]


# Media Files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default Primary Key Field Type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = "sop.CustomUser"
