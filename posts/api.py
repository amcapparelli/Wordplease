from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog
from posts.models import Post
from posts.serializers import PostSerializers


class APISingleBlogView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        posts = Post.objects.filter(blog=pk)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user_blog = Blog.objects.get(author=self.request.user)
        serializer.save(blog=user_blog)


