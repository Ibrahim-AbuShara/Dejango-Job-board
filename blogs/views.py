from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
def blog_list(request):
    blogs=Blog.objects.all()
    paginator=Paginator(blogs,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html',{'blogs':page_obj})