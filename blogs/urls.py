from django.urls import path
from . import views
app_name='blogs'
urlpatterns = [
    
    path('',views.blog_list, name='blogs'),
    path('blogpost/',views.post_blog, name='blogpost'),
    ]