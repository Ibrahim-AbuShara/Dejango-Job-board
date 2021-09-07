from accounts.models import Profile
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import Profile_Data, Signup, User_Data
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse


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
            return redirect(reverse('accounts:editprofile'))

    else:
        form=Signup()
    return render(request,'registration/signup.html',{'form':form})

def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'UI/profile.html',{'profile':profile})


def edit (request):
    profile=Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        userform =User_Data(request.POST,instance=request.user)
        profileform=Profile_Data(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
        return redirect(reverse('accounts:profile'))            
           
    else:
        userform =User_Data(instance=request.user)
        profileform=Profile_Data(instance=profile)
    return render(request,'UI/editprofile.html',{'profile':profileform,'user':userform})