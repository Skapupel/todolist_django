from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    This is a User Model, that is used to create a table in the database.\n
    
    This model inherits from BaseUser model provided by django.
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        """Returns a string representation of the User Model.

        Returns:
            str: returns a username
        """
        return self.username
