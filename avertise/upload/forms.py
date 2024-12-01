from django import forms
from .models import CompletedWork

class CompletedWorkForm(forms.ModelForm):
    class Meta:
        model = CompletedWork
        fields = ['file']
