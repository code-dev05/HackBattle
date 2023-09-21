from django.http import HttpResponseBadRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import uploadfileform
from random import randint
from django.conf import settings

user_name=None

# Create your views here.
def base(request):
    return render(request, 'base.html', {})

def home(request):
    form = uploadfileform()
    if request.method == "POST":
        form = uploadfileform(request.POST,request.FILES)
        if form.is_valid():
            handle_file(request.FILES['file'])
        else:
            form = uploadfileform()
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_name = username
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('home')
        else:
            user_name = None
            print("works")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def file_upload(request):
    if request.method == "POST":
        form = uploadfileform(request.POST, request.FILES)
        if form.is_valid():
            if "file" in request.FILES:
                handle_file(request.FILES["file"])
            else:
                return HttpResponseBadRequest("No 'file' key found in uploaded files.")
        else:
            return HttpResponseBadRequest("Invalid form data.")
    
    # Handle GET requests or other cases where the form is not valid.
    return HttpResponseBadRequest("Invalid request.")


def handle_file(f):
    with open('static/upload/' + f.name, 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)