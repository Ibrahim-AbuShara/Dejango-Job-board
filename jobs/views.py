from typing import ContextManager
from django.shortcuts import render
from .models import jobs
from django.core.paginator import Paginator

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
   context={'job':job_detalis}
   return render(request,'jobs/job_ditales.html',context)