from rest_framework.permissions import BasePermission

from blogs.models import Blog


class PostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            user_blog = Blog.objects.get(author=request.user)
        except Blog.DoesNotExist:
            user_blog = None
        return request.method == 'GET' or obj.blog == user_blog or request.user.is_superuser
