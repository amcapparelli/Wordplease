from django.urls import path

from blogs.views import BlogListView, UserPageView
from posts.views import PostListView, NewPostView, SinglePostView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('blogs', BlogListView.as_view(), name='blog_list'),
    path('new-post', NewPostView.as_view(), name='new_post'),
    path('blogs/<username>', UserPageView.as_view(), name='user_page'),
    path('blogs/<username>/<int:pk>', SinglePostView.as_view(), name='single_post')
]