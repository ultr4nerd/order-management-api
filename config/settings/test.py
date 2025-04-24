"""
With these settings, tests run faster.
"""

from .base import *  # noqa: F403
from .base import TEMPLATES
from .base import env

# GENERAL
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="ALrl1gEsOe7FIuJz5Pcu8B3lfzzau9D7Ivh7yer0bE9CxvDce0iod4w7i9jmausf",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# DEBUGGING FOR TEMPLATES
TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore[index]

# MEDIA
MEDIA_URL = "http://media.testserver/"
