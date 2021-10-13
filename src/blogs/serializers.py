from rest_framework import  serializers
from .models import Blog,Comment
class blog_serializers(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields ='__all__'


class Comment_serilizers(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'