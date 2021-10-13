from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Blog,Comment
from .serializers import blog_serializers,Comment_serilizers

#class basedviwes
class Blog_API(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class= blog_serializers

class BLOG_Ditali_API(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=blog_serializers
    lookup_field='id'


class Comments_API(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=Comment_serilizers
    