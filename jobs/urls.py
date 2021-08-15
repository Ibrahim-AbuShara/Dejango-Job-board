from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
app_name='jobs'
urlpatterns = [
    
    path('',views.job_list),
    path('<str:slug>',views.job_detalis,name='job_detalis'),
    
]
