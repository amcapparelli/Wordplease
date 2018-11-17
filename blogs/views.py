from django.shortcuts import render
from django.views import View

from blogs.models import Blog


class BlogListView(View):
    def get(self, request):
        all_blogs = Blog.objects.all().select_related('author')
        context = {'blogs': all_blogs}
        return render(request, 'blogs/index.html', context)


