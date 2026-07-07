from .settings import *
import os

# Production overrides
DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',') if os.environ.get('ALLOWED_HOSTS') else ['*']

# Database configuration via env vars (defaults to sqlite)
if os.environ.get('DB_ENGINE'):
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT', ''),
        }
    }

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add WhiteNoise middleware just after SecurityMiddleware
MIDDLEWARE = MIDDLEWARE.copy()
try:
    idx = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1
except ValueError:
    idx = 0
MIDDLEWARE.insert(idx, 'whitenoise.middleware.WhiteNoiseMiddleware')
