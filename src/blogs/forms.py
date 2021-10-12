from django import forms
from .models import Blog, Comment

class Blog_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['title','img','head_line','subject']
class Comment_form(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)
