from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE)
    phone=PhoneNumberField()
    country=CountryField()
    img=models.ImageField(upload_to='images/')
    birth_date = models.DateField('Date of Birth', null=True, blank=True)
   
    @receiver(post_save, sender=User)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    def __str__(self) -> str:
        return str(self.user)

    
