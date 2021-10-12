from collections import UserDict
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.utils.text import slugify
from django.contrib.auth.models import User
Job_Type=(('full time','part time'),('part time','full time'))
Gander=(('male','male'),('female','female'),('male/female','male/female'))

class Category(models.Model):
    cataegoty=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.cataegoty




class jobs(models.Model):
    user=models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    title=CharField(max_length=50)
    job_type=CharField(max_length=20, choices=Job_Type)
    description=models.TextField(max_length=1500)
    published_at=models.DateTimeField(auto_now=True)
    vacancy= models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    excprince =models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=CASCADE)
    img = models.ImageField(max_length=256, upload_to='jobs/')
    Gander=CharField(max_length=20,choices=Gander)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(jobs,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title

class Apply(models.Model):
    job =models.ForeignKey(jobs,related_name='apply_job',on_delete=CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    website=models.URLField()
    cv=models.FileField(upload_to='cvs/')
    letter=models.TextField(max_length=1500)
    Apply_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name



