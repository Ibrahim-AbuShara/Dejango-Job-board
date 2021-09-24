from jobs.filters import JobFilter
from jobs.models import jobs
from django.shortcuts import render

# Create your views here.

   

def home(request):
    job_list=jobs.objects.all()
    counter=job_list.count()
    filter=JobFilter(request.GET,queryset=job_list)
    job_list=filter.qs
    context={"jobs":job_list,"counter":counter,'filter':filter}
    return render(request,'home/index.html',context)

