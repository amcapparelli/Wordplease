from django.urls import path

from blogs.views import UserPageView
from posts.api import APISingleBlogView, APISinglePostView
from posts.views import NewPostView, SinglePostView

urlpatterns = [

    path('new-post', NewPostView.as_view(), name='new_post'),
    path('blogs/<username>', UserPageView.as_view(), name='user_page'),
    path('blogs/<username>/<int:pk>', SinglePostView.as_view(), name='single_post'),

    #API Routes
    path('api/1.0/blog/<username>', APISingleBlogView.as_view(), name='API_single_blog'),
    path('api/1.0/blog/<username>/<int:pk>', APISinglePostView.as_view(), name='API_single_post')

]