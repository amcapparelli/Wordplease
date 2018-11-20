from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views import View

from blogs.models import Blog
from posts.models import Post
from posts.newPostForm import PostForm


class PostListView(View):
    def get(self, request):
        latest_posts = Post.objects.all().select_related('blog').order_by('-date_published')
        context = {'posts': latest_posts}
        return render(request, 'home.html', context)

class NewPostView(View):

    def get(self, request):
        form = PostForm()
        return render(request, 'new-post.html', {'new_post': form})

    def post(self, request):
        blog = Blog.objects.get(author=request.user)
        post = Post(blog=blog)
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
        return render(request, 'new-post.html', {'new_post': form})