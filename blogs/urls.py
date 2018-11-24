from django.urls import path

from blogs.api import BlogsListApiView
from blogs.views import BlogListView
from posts.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('blogs', BlogListView.as_view(), name='blog_list'),

    #API Routes
    path('api/1.0/blogs', BlogsListApiView.as_view(), name='API_blogs_view')
]