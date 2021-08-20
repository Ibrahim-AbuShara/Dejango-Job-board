from jobs.forms import Apply_job
from typing import ContextManager
from django.shortcuts import render
from .models import jobs,Apply
from django.core.paginator import Paginator
from django import forms

# Create your views here.
def job_list(request):
    job_list=jobs.objects.all()
    paginator = Paginator(job_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"jobs":page_obj}
    return render(request,'jobs/job_list.html',context)


def job_detalis(request,slug):
   job_detalis=jobs.objects.get(slug=slug)
   if request.method == 'POST':
       form=Apply_job(request.POST , request.FILES )
       if form.is_valid():
           print('valid')
           myform=form.save(commit=False)
           myform.job=job_detalis
           myform.save()
           
   else:
        form = Apply_job()


   context={'job':job_detalis,'form':form}
   return render(request,'jobs/job_ditales.html',context)