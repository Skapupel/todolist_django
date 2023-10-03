from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from drf_spectacular import openapi


@extend_schema_view(
    get=extend_schema(
        description="List all todo items. Only authenticated users are allowed."
    ),
    post=extend_schema(
        description="Create a new todo item. Only authenticated users are allowed.",
    )
)
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


@extend_schema_view(
    get=extend_schema(
        parameters=[
            openapi.OpenApiParameter(
                "id",
                openapi.OpenApiTypes.INT,
                location=openapi.OpenApiParameter.PATH,
                required=True,
                description="The id of the todo item.",
            )
        ],
        description="Detail of a todo item. Only authenticated users are allowed."
    ),
    put=extend_schema(
        parameters=[
            openapi.OpenApiParameter(
                "id",
                openapi.OpenApiTypes.INT,
                location=openapi.OpenApiParameter.PATH,
                required=True,
                description="The id of the todo item.",
            )
        ],
        description="Update a todo item. Only authenticated users are allowed.",
    ),
    patch=extend_schema(
        parameters=[
            openapi.OpenApiParameter(
                "id",
                openapi.OpenApiTypes.INT,
                location=openapi.OpenApiParameter.PATH,
                required=True,
                description="The id of the todo item.",
            )
        ],
        description="Partial update of a todo item. Only authenticated users are allowed.",
    ),
    delete=extend_schema(
        parameters=[
            openapi.OpenApiParameter(
                "id",
                openapi.OpenApiTypes.INT,
                location=openapi.OpenApiParameter.PATH,
                required=True,
                description="The id of the todo item.",
            )
        ],
        description="Delete a todo item. Only authenticated users are allowed.",
    )
)
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
