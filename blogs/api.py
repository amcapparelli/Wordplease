from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog
from blogs.serializers import BlogsViewSerializer


class BlogsListApiView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogsViewSerializer(blogs, many=True)
        return Response (serializer.data)