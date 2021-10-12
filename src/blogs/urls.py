from django.urls import path
from . import views
app_name='blogs'
urlpatterns = [
    
    path('',views.blog_list, name='blogs'),
    path('blogpost/',views.post_blog, name='blogpost'),
    path('<int:id>',views.blog_detail, name='blog_detail'),

    ]