from django.contrib import admin

from .models import User

# Adds User model to the admin site
admin.site.register(User)
