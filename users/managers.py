from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    This class creates a UserManager that inherits from BaseUserManager provided by Django.\\
    It is used to apply some easy to use commands to create a user or superuser.
    """
    def create_user(self, username, password=None, **extra_fields):
        """
        Creates a user in database.

        Args:
            username (str): Username field.
            password (str, optional): Password field. Defaults to None.

        Raises:
            ValueError: If username filed is not set.

        Returns:
            User: Returns a user object.
        """
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Create a superuser in database.

        Args:
            username (str): Username field.
            password (str, optional): Password field. Defaults to None.

        Returns:
            User: Returns a user object.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)
