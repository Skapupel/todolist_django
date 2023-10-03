from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    Registers a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserView(generics.RetrieveAPIView):
    """
    Returns a current user object. Only authenticated users are allowed.
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

