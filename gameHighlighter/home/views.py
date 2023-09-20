from django.http import HttpResponseBadRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import uplodfileform

user_name=None

# Create your views here.
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
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user_name= username
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
    dbx = dropbox.Dropbox("sl.BmYrGRUJSvIosQVs6YtxSlHjA7jByYi8f5Owz-T_MsSKkJgAyK3-RX4yE_gmS1X2kSEoCUcf9YLnX7iI5bGBYoh5F70IfKzwA6BpaTuRlKGICadLkpT_WeoO57mcfh3ZZVz473dcXtzWYvGAlxOgTN4")

   
   
    with open('static/upload/' + f.name, 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

    file_from = 'C:/Users/devan/Data/Hackathon Projects/HackBattle/gameHighlighter/static/upload/' + f.name

    file_to = '/hello/video100.mp4'
    

    ft = open(file_from, 'rb')
    dbx.files_upload(ft.read(), file_to)
