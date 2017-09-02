from django.contrib import admin
from .models import Post # Imports Post model from models file in same directory

# Register your models here.
admin.site.register(Post)
