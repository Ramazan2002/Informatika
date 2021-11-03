from django.contrib import admin
from .models import Post, Comment
from users.admin import MyModelAdmin
# Register your models here.

admin.site.register(Post, MyModelAdmin)
admin.site.register(Comment)