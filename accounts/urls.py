from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
app_name='account'
urlpatterns = [
    
    path('signup',views.sign_up, name='signup'),
    path('profile',views.profile, name='profile')
    
    
    
]
