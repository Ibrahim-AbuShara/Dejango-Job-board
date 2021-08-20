from django import forms
from .models import Apply

class Apply_job(forms.ModelForm):
    class  Meta:
        model=Apply
        fields=['name','email','website','cv','letter']