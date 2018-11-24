from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from blogs.NewBlogForm import NewBlogForm
from blogs.models import Blog
from posts.models import Post


class BlogListView(View):
    def get(self, request):
        all_blogs = Blog.objects.all().select_related('author')
        context = {'blogs': all_blogs}
        return render(request, 'blogs/index.html', context)

class UserPageView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        try:
            user_blog = Blog.objects.get(author=user)
            posts = Post.objects.filter(blog=user_blog).order_by('-date_published')
            context = {'posts': posts}
            return render(request, 'blogs/user_page.html', context)
        except Blog.DoesNotExist:
            form = NewBlogForm()
            context = {'new_blog': form}
            return render(request, 'blogs/create_blog.html', context)

    def post(self, request, username):
        blog = Blog(author=request.user, blog_url='blogs/' + username)
        form = NewBlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('new_post')
