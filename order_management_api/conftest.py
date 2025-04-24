import pytest
from model_bakery import baker

from order_management_api.users.models import User


@pytest.fixture
def user(db) -> User:
    return baker.make_recipe("users.user")
