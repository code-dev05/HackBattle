from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("works")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')