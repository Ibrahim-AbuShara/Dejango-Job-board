from django.forms import fields
from accounts.models import Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
class User_Data(forms.ModelForm):
    class Meta:
        model =User
        fields=['first_name','last_name']
        


class Profile_Data(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude=['user']