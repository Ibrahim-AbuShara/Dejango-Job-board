from typing import ContextManager
from django.shortcuts import render
from .models import jobs
# Create your views here.
def job_list(request):
    job_list=jobs.objects.all()
    context={"jobs":job_list}
    return render(request,'jobs/job_list.html',context)


def job_detalis(request,id):
   job_detalis=jobs.objects.get(id=id)
   context={'job':job_detalis}
   return render(request,'jobs/job_ditales.html',context)