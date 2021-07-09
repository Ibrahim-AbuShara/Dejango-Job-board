from django.contrib import admin

# Register your models here.
from .models import  Category, jobs
admin.site.register(jobs)
admin.site.register(Category)