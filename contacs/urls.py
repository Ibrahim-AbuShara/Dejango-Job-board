from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
app_name='contacs'
urlpatterns = [
    
    path('',views.contact, name='job_list'),
   
    
]
