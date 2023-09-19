from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.home, name='homebyid'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
