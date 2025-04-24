# ruff: noqa: E501
from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import env

# GENERAL
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="PrWxkoeW7b7x9LPIcklJZ9PQ6IuUv5b1VJaWIrGc7vkt01XGUpVnBQk0wivkhAnO",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # noqa: S104

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    },
}

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

# Whitenoise
INSTALLED_APPS = ["whitenoise.runserver_nostatic", *INSTALLED_APPS]

# Django Extensions
INSTALLED_APPS += ["django_extensions"]
