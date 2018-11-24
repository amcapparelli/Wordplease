from rest_framework.generics import ListAPIView

from blogs.models import Blog
from blogs.serializers import BlogsViewSerializer


class BlogsListApiView(ListAPIView):

    serializer_class = BlogsViewSerializer

    def get_queryset(self):
        author = self.request.query_params.get('author', None)
        order = self.request.query_params.get('order', None)
        if author is not None and order is not None:
            return Blog.objects.filter(author__username=author).order_by(order)
        if author is not None:
            return Blog.objects.filter(author__username=author)
        if order is not None:
            return Blog.objects.all().order_by(order)
        return Blog.objects.all()

