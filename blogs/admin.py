from django.contrib import admin

# Register your models here.
from blogs.models import Blog

@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['blog_title', 'author_fullname', 'date_created']

    def author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)