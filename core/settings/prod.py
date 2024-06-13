from .base import BASE_DIR
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ei9z54p3f+^d!w+al=6gq!3=8_%4y$%96$0rt4zkwz^_vn*&q_'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(
    BASE_DIR, "/home/pujanraj/zebabeauty.itnepalsolutions.com/media/")
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(
    BASE_DIR, "/home/pujanraj/zebabeauty.itnepalsolutions.com/media/")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
