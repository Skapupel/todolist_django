from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Get the list of items for this view, filtered by an authenticated user.
        """
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Creates a model instance, filtered by an authenticated user.
        """
        serializer.save(user=self.request.user)


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Get the list of items for this view, filtered by an authenticated user.
        """
        return Todo.objects.filter(user=self.request.user)
