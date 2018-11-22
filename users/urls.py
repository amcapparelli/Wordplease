from django.urls import path

from users.api import UsersDetailApiView, UserRegisterApi
from users.views import LoginView, LogoutView, SignUpView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignUpView.as_view(), name='signup'),

    #API routes
    path('api/1.0/users/<int:pk>', UsersDetailApiView.as_view(), name='API_users_detail_view'),
    path('api/1.0/users/signup', UserRegisterApi.as_view(), name='API_users_register')
]