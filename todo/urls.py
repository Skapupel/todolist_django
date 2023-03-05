from django.urls import path
from .views import TodoListCreateAPIView, TodoDetailAPIView


urlpatterns = [
    path('user/todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('user/todos/<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
]
