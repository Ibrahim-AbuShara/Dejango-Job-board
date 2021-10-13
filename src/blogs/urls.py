from django.urls import path
from . import views
from . import api
app_name='blogs'
urlpatterns = [
    
    path('',views.blog_list, name='blogs'),
    path('blogpost/',views.post_blog, name='blogpost'),
    path('<int:id>',views.blog_detail, name='blog_detail'),

    #--------------------------API---------------------------
    path('api/blogs_api',api.Blog_API.as_view(), name='blogs_api'),
    path('api/<int:id>',api.BLOG_Ditali_API.as_view(), name='blogs_api'),
    path('api/blogs_comments',api.Comments_API.as_view(), name='blogs_comments'),

    ]