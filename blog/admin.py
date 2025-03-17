from django.contrib import admin
from .models import BlogPost, Like, Reply, Comment
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Like)
admin.site.register(Reply)
admin.site.register(Comment)