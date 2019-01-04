from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from blogs.models import Blog
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializers


class APISingleBlogView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        try:
            user_blog = Blog.objects.get(author=user)
        except Blog.DoesNotExist:
            content = {'{0}'.format(user): 'this user has no blog yet'}
            return Response(content)

        key_word = self.request.query_params.get('search') or ''
        if request.user.is_authenticated and request.user == user:
            posts = Post.objects.filter(
                Q(post_title__contains=key_word) | Q(post_body__contains=key_word),
                blog=user_blog,
                ).order_by('-date_published')
            serializer = PostSerializers(posts, many=True)
            return Response(serializer.data)
        else:
            today = datetime.today()
            posts = Post.objects.filter(
                Q(post_title__contains=key_word) | Q(post_body__contains=key_word),
                blog=user_blog, date_published__lte=today,
            ).order_by('-date_published')
            serializer = PostSerializers(posts, many=True)
            return Response(serializer.data)

    def perform_create(self, serializer):
        user_blog = Blog.objects.get(author=self.request.user)
        serializer.save(blog=user_blog)

class APISinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated, PostPermission]
