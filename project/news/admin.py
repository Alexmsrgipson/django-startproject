from django.contrib import admin
from .models import Categories, Post, Author, Comment

# Register your models here.
admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Author)