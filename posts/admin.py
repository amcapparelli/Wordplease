from django.contrib import admin

# Register your models here.
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'blog', 'date_published']
    list_filter = ['blog']
    search_fields = ['post_title']