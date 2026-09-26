from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class AuthTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="vanger", password="vanger", role=User.Role.VIEWER)

    def test_login_with_Right_creds(self):
        response = self.client.post("/api/auth/login/", {"username": "vanger", "password":"vanger"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_with_Wrong_creds(self):
        response = self.client.post("/api/auth/login/", {"username": "NotVanger", "password": "NotVanger"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_requires_auth(self):
        response = self.client.get("/api/auth/me/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_me_return_role(self):
        self.client.force_authenticate(self.user)
        response = self.client.get("/api/auth/me/")
        self.assertEqual(response.data["role"], ["VIEWER"])
