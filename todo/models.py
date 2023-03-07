from users.models import User
from django.db import models


class Todo(models.Model):
    """
    This is a Todo Model, that is used to create a table in the database.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the Todo Model.

        Returns:
            str: returns a todo title
        """
        return self.title
