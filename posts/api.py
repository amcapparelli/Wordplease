from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializers


class APISingleBlogView(APIView):
    def get(self, request, pk):
        posts = Post.objects.filter(blog=pk)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)

