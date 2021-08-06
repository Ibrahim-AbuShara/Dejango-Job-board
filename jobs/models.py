from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
Job_Type=(('full time','part time'),('part time','full time'))
# Create your models here.
class Category(models.Model):
    cataegoty=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.cataegoty

def img_name(instance,fn):
    name='jobs/%s.png'% instance.id
    return name


class jobs(models.Model):
    title=CharField(max_length=50)
    job_type=CharField(max_length=20, choices=Job_Type)
    description=models.TextField(max_length=1500)
    published_at=models.DateTimeField(auto_now=True)
    vacancy= models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    excprince =models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=CASCADE)
    img = models.ImageField(max_length=256, upload_to=img_name)

    def __str__(self) -> str:
        return self.title
