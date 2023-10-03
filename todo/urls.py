from django.urls import path
from .views import TodoListCreateAPIView, TodoDetailAPIView


# Endpoints
urlpatterns = [
    path('', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
]
