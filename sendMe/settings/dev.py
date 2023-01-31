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

STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')