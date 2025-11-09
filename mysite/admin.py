from django.contrib import admin # contrib module is imported for admin interface
from .models import Task # Task model is imported from models module
admin.site.register(Task) # Task model is registered with the admin site