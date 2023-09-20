from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import uplodfileform

user_name=None

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
        form = uplodfileform(request.POST,request.FILES)
        if form.is_valid():
            handle_file(request.FILES["file"])


def handle_file(f):
    import dropbox
    dbx = dropbox.Dropbox("sl.BmaZxI4b2AB7dyQt6p_UdM7_ZyZSsUyrOlP4ONW-atIApmbas97qOD_G771_SymS_7DcHMREYiyaXEuX5mQO5W4Fswouryp5ZAQCUlXowd60-0YIzz3p83RpJsl01EGH46-l7EONMganrAp71YCyKfU")


    
    file_to = '/hello/'+user_name
 

    ft = open(f, 'rb')
    dbx.files_upload(ft.read(), file_to)

       
