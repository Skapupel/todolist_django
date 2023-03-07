from django.contrib import admin
from .models import Todo

# Adds Todo model to the admin site
admin.site.register(Todo)
