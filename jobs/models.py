from django.db import models

# Create your models here.
class jobs(models.Model):
    title = models.CharField(max_length=100) #column
