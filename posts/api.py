from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

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
        user_blog = Blog.objects.get(author=user)
        posts = Post.objects.filter(blog=user_blog)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user_blog = Blog.objects.get(author=self.request.user)
        serializer.save(blog=user_blog)

class APISinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly, PostPermission]

