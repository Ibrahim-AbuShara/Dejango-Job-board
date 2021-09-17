from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    if request.method=='POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
                  subject,
                  message,
                  email,
                 [settings.EMAIL_HOST_USER],
                 fail_silently=True,
                 
                 )
    return render(request,'contact.html')