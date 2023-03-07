from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    Concrete view for creating a model instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserView(generics.RetrieveAPIView):
    """
    Concrete view for retrieving a model instance.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Returns the object the view is displaying.

        Returns:
            User: return a user object.
        """
        return self.request.user

