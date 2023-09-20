from django.http import HttpResponseBadRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import uplodfileform
from random import randint

user_name=None

# Create your views here.
def base(request):
    return render(request, 'base.html', {})

def home(request):
    form = uplodfileform()
    if request.method == "POST":
        form = uplodfileform(request.POST,request.FILES)
        if form.is_valid():
            handle_file(request.FILES['file'])
        else:
            form = uplodfileform()
    return render(request, 'home.html', {'form': form})

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
        form = uplodfileform(request.POST, request.FILES)
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
    import dropbox
    dbx = dropbox.Dropbox("sl.Bmb8iT5vhBmN2qzEEDvdMSh-MUqfP07RXmmUZDAZHZ2h0Cp61QLqD6__hJSqrXIufrdBcEjD8UTBipcVDBQYmUenX9wxZT86O_7fRegqXzZG4vruxNWQh2WPXIWyIAUpmRl55bWPP7gjtMczKOvSAxA")
   
    with open('static/upload/' + f.name, 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

    file_from = 'C:/Users/devan/Data/Hackathon Projects/HackBattle/gameHighlighter/static/upload/' + f.name

    file_to = f'/hello/{user_name}-{randint(0, 10000)}.mp4'
    
    ft = open(file_from, 'rb')
    dbx.files_upload(ft.read(), file_to)
