from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from .models import Todo
from users.models import User


class TodoListCreateAPIViewTest(APITestCase):
    """
    A todo create and list unit test class.
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
        self.url = reverse('todo-list-create')

        self.todo_data = {
            'title': 'Test Todo',
            'completed': False
        }

    def test_todo_list_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_todo_list_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_create_unauthenticated(self):
        response = self.client.post(self.url, self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_todo_create_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(self.url, self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TodoDetailAPIViewTest(APITestCase):
    """
    A todo get, update and delete unit test class.
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

        self.todo = Todo.objects.create(
            user=self.user,
            title='Test Todo',
            completed=False
        )

        self.todo_data = {
            'title': 'Updated Test Todo',
            'completed': True
        }

    def test_todo_retrieve_unauthenticated(self):
        response = self.client.get(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_todo_retrieve_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_update_unauthenticated(self):
        response = self.client.put(reverse('todo-detail', kwargs={'pk': self.todo.id}), self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_todo_update_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.put(reverse('todo-detail', kwargs={'pk': self.todo.id}), self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo_data['title'])
        self.assertEqual(response.data['completed'], self.todo_data['completed'])

    def test_todo_delete_unauthenticated(self):
        response = self.client.delete(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_todo_delete_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.delete(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())
