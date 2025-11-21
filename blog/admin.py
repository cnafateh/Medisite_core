from django.contrib import admin
from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'is_published', 'published_at', 'created_by')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'summary', 'content')
