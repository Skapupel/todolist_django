from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class UserRegistrationViewTest(APITestCase):
    """
    A user registration unit test class.
    """

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }

    def test_create_user(self):
        response = self.client.post(reverse('user_registration'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserViewTest(APITestCase):
    """
    A user login and info unit test class.
    """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

    def test_get_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
