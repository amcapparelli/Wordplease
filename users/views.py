from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from users.signupForm import SignupForm


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ups... Invalid username or password')
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class SignUpView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'signup_form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.username = form.cleaned_data.get('username')
            user.set_password(form.cleaned_data.get('password'))
            user.save()
        return render(request, 'signup.html', {'signup_form': form})
