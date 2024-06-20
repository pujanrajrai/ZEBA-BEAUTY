from .base import BASE_DIR
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-r4c#qh16z_mxuce$pgs+a+l0_56ion)rr&1p@c4sm_3lv$3eyp"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
APPEND_SLASH = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
