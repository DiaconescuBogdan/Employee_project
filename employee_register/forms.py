from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname':'Full Name',
            'emp_code':'Emp Code'
        }