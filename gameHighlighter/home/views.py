from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
login = 0
def home(request, id=0):
    if request == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login = 1
        return HttpResponseRedirect('/')
    login = id
    return render(request, 'home.html', {'login': login})

def about(request):
    return render(request, 'about.html', {'login': login})

def login(request):
    return render(request, 'login.html', {'login': login})

def register(request):
    return render(request, 'register.html')