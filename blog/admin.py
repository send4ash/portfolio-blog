from django.contrib import admin
from .models import Post, Comment # Imports Post and Comment models from models file in same directory

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
