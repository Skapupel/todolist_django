from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    This is a serializer for a model called Todo.
    It defines the fields that will be included in the serialized output when the Todo model is serialized.
    """
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'created_at')
