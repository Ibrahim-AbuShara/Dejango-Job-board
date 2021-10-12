from django.shortcuts import redirect, render
from django.urls.base import reverse
from blogs.forms import Blog_form
from .models import Blog,Comment
from django.core.paginator import Paginator
from .forms import Blog_form,Comment_form

def blog_list(request):
    blogs=Blog.objects.all()
    paginator=Paginator(blogs,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html',{'blogs':page_obj})


def post_blog(request):
    
    if request.method == 'POST':
        form = Blog_form(request.POST, request.FILES) 
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect(reverse('blogs:blogs'))
    else:
        form=Blog_form()
        return render(request,'bolg_post.html',{'form':form})

def blog_detail(request,id):
    blog=Blog.objects.get(id=id)
    coment_static=Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        form=Comment_form(request.POST , request.FILES )
        if form.is_valid():
            print('valid')
            myform=form.save(commit=False)
            myform.user=request.user
            myform.blog=blog
            myform.save()
            return redirect(reverse('blogs:blogs'))

            
    else:
        comment=Comment_form()
        return render(request,'blogl_detales.html',{"blog":blog,'form':comment,"comments":coment_static})




