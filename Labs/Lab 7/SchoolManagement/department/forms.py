from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'head']
        labels = {
            'name': 'اسم القسم',
            'head': 'رئيس القسم',
        }
