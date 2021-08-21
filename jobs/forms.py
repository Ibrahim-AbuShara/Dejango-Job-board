from django import forms
from .models import Apply,jobs

class Apply_job(forms.ModelForm):
    class  Meta:
        model=Apply
        fields=['name','email','website','cv','letter']



class Post_job(forms.ModelForm):
    class Meta:
        model=jobs
        fields=['title','job_type','description','vacancy','salary','excprince','category','img']        