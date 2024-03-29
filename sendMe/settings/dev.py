from pathlib import Path
import os

DEBUG = True

STATIC_URL = '/assets/'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
ALLOWED_HOSTS = [
    '192.168.31.242',
    '127.0.0.1',
    '192.168.1.103',
    'localhost'
]

# postgre database configuration
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'sendme',
    'USER': 'samad',
    'PASSWORD': '867140',
    'HOST': '127.0.0.1',
    'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static/media'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')