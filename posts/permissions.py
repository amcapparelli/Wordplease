from rest_framework.permissions import BasePermission

from blogs.models import Blog


class PostPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated or request.method == 'GET'
        pass

    def has_object_permission(self, request, view, obj):
        user_blog = Blog.objects.get(author=request.user)
        return request.method == 'GET' or obj.blog == user_blog or request.user.is_superuser
