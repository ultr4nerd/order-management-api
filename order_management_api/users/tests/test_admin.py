"""Tests for the users app admin."""

from django.urls import reverse
from rest_framework import status

from order_management_api.users.models import User


class TestUserAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:users_user_changelist")
        response = admin_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_search(self, admin_client):
        url = reverse("admin:users_user_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == status.HTTP_200_OK

    def test_add(self, admin_client):
        url = reverse("admin:users_user_add")
        response = admin_client.get(url)
        assert response.status_code == status.HTTP_200_OK

        response = admin_client.post(
            url,
            data={
                "email": "new-admin@parrotsoftware.io",
                "password1": "My_R@ndom-P@ssw0rd",
                "password2": "My_R@ndom-P@ssw0rd",
            },
        )
        assert response.status_code == status.HTTP_302_FOUND
        assert User.objects.filter(email="new-admin@parrotsoftware.io").exists()

    def test_view_user(self, admin_client):
        user = User.objects.get(email="admin@example.com")
        url = reverse("admin:users_user_change", kwargs={"object_id": user.pk})
        response = admin_client.get(url)
        assert response.status_code == status.HTTP_200_OK
