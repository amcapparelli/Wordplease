from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


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
        return render(request, 'signup.html')