from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from . import api
app_name='jobs'
urlpatterns = [
    
    path('',views.job_list, name='job_list'),
    path('post',views.post,name='post_job'),
    path('<str:slug>',views.job_detalis,name='job_detalis'),
    
    #api
    path('api/jobs',api.joblist_api,name='jobs'),
    path('api/jobs/<int:id>',api.jobdital_api,name='job ditail'),
    
]
