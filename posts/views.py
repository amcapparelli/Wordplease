from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from blogs.models import Blog
from posts.models import Post
from posts.newPostForm import PostForm


class PostListView(View):
    def get(self, request):
        latest_posts = Post.objects.all().select_related('blog').order_by('-date_published')
        context = {'posts': latest_posts}
        return render(request, 'home.html', context)

class NewPostView(LoginRequiredMixin, View):

    login_url = '/login'

    def get(self, request):
        blog = Blog.objects.filter(author=request.user).exists()
        if blog == True:
            form = PostForm()
            return render(request, 'new-post.html', {'new_post': form})
        else:
            return redirect('user_page', username=request.user)


    def post(self, request):
        blog = Blog.objects.get(author=request.user)
        post = Post(blog=blog)
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            form = PostForm()
        return render(request, 'new-post.html', {'new_post': form})

class SinglePostView(DetailView):

    model = Post
    template_name = 'single_post.html'