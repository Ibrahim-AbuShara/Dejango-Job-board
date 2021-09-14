import django_filters
from .models import jobs
class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
   
    class Meta:
        model = jobs
        fields =['title','excprince','category','job_type','Gander']
        