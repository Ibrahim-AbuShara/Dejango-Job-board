from django.contrib import admin

# Register your models here.
from .models import  Category, jobs,Apply
admin.site.register(jobs)
admin.site.register(Category)
admin.site.register(Apply)