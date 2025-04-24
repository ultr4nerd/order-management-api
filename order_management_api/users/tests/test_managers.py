"""Module with tests for the UserManager."""

from io import StringIO

import pytest
from django.core.management import call_command

from order_management_api.users.baker_recipes import COMMON_PASSWORD
from order_management_api.users.models import User


@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        user = User.objects.create_user(
            email="john@parrotsoftware.io",
            password=COMMON_PASSWORD,
        )
        assert user.email == "john@parrotsoftware.io"
        assert not user.is_staff
        assert not user.is_superuser
        assert user.check_password(COMMON_PASSWORD)
        assert user.username is None

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="admin@parrotsoftware.io",
            password=COMMON_PASSWORD,
        )
        assert user.email == "admin@parrotsoftware.io"
        assert user.is_staff
        assert user.is_superuser
        assert user.username is None

    def test_create_superuser_username_ignored(self):
        user = User.objects.create_superuser(
            email="test@parrotsoftware.io",
            password=COMMON_PASSWORD,
        )
        assert user.username is None

    def test_create_user_with_no_email(self):
        """Test creating a user with no email raises ValueError."""
        with pytest.raises(ValueError, match="The given email must be set"):
            User.objects.create_user(email="", password=COMMON_PASSWORD)

    def test_create_superuser_with_is_staff_false(self):
        """Test creating a superuser with is_staff=False raises ValueError."""
        with pytest.raises(ValueError, match="Superuser must have is_staff=True"):
            User.objects.create_superuser(
                email="stafffalse@parrotsoftware.io",
                password=COMMON_PASSWORD,
                is_staff=False,
            )

    def test_create_superuser_with_is_superuser_false(self):
        """Test creating a superuser with is_superuser=False raises ValueError."""
        with pytest.raises(ValueError, match="Superuser must have is_superuser=True"):
            User.objects.create_superuser(
                email="superuserfalse@parrotsoftware.io",
                password=COMMON_PASSWORD,
                is_superuser=False,
            )


@pytest.mark.django_db
def test_createsuperuser_command():
    """Ensure createsuperuser command works with our custom manager."""
    out = StringIO()
    command_result = call_command(
        "createsuperuser",
        "--email",
        "henry@parrotsoftware.io",
        interactive=False,
        stdout=out,
    )

    assert command_result is None
    assert out.getvalue() == "Superuser created successfully.\n"
    user = User.objects.get(email="henry@parrotsoftware.io")
    assert not user.has_usable_password()
