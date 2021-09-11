from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth import  login,logout
app_name='accounts'
urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('signup/',views.sign_up, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('editprofile/',views.edit, name='editprofile'),
    
    
    
]
