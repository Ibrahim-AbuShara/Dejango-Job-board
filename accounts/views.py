from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import Signup
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def sign_up(request):
    
    if request.method == 'POST':
        form=Signup(request.POST )
        if form.is_valid():
            form.save()
            user=form.cleaned_data['username']
            password=form.cleaned_data['password2']
            auth=authenticate(username=user,password=password )
            login(request,auth)
            return redirect('/accoutns/profile')

    else:
        form=Signup()
    return render(request,'registration/signup.html',{'form':form})

def profile(request):
    pass