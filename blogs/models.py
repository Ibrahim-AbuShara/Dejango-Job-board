from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    user=models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    img = models.ImageField(upload_to='blogs/')
    head_line=models.TextField(max_length=50)
    published_at=models.DateTimeField(auto_now=True)
    subject = models.TextField(blank=True)
    def __str__(self) -> str:
        return self.title

class  Comment(models.Model):
        user=models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
        comment = models.TextField()
        published_at=models.DateTimeField(auto_now=True)
        blog=models.ForeignKey(Blog, verbose_name=("blog"), on_delete=models.CASCADE)
        def __str__(self) -> str:
            return str(self.blog)
        


