from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),
    path('', views.home, name='upload_file'),
]
