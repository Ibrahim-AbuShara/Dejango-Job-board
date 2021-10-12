from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import jobs
from .serializers import JobSerializer

@api_view()
def joblist_api(request):
   job_list_data=jobs.objects.all()
   api=JobSerializer(job_list_data , many=True).data
   return Response ({'api':api})
    

@api_view()
def jobdital_api(request,id):
    job=jobs.objects.get(id=id)
    data=JobSerializer(job).data
    return Response({'data':data})