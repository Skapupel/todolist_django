from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    This is a serializer for a model called User.
    It defines the fields that will be included in the serialized output when the User model is serialized.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        """
        Raises when the user is going to be created with serializer.\\
        Creates a user in database.

        Args:
            validated_data (dict): Data that was sent to serializer.

        Returns:
            User: Returns a user object.
        """
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

