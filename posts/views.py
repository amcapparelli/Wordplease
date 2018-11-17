from django.shortcuts import render

# Create your views here.
from django.views import View

from posts.models import Post


class PostListView(View):
    def get(self, request):
        latest_posts = Post.objects.all().select_related('blog').order_by('-date_published')
        context = {'posts': latest_posts}
        return render(request, 'home.html', context)