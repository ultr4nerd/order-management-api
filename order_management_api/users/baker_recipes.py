"""Users app baker recipes."""

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from model_bakery.random_gen import gen_email
from model_bakery.recipe import Recipe

_UserModel = get_user_model()

COMMON_PASSWORD = "M1F4k3P4ssword!"  # noqa: S105


def gen_password() -> str:
    return make_password(COMMON_PASSWORD)


user = Recipe(
    _UserModel,
    email=gen_email,
    password=gen_password,
)
