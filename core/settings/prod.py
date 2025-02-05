from .base import *
from decouple import config
import os
from datetime import timedelta


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2k#89%%zdm$+j_7u(yr8sp4%e&tm0+1rufyrnbs*s6964jyap*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(
    BASE_DIR, "/home/pujanraj/zebabeautysalon.com/media")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, "/home/pujanraj/zebabeautysalon.com")


ALLOWED_HOSTS = [
    "*"
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
