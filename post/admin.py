from django.contrib import admin
from .models import Post, PostFile

class PostFileInline(admin.TabularInline):
    model = PostFile
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at')
    inlines = [PostFileInline]

@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'file')

