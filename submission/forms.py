from django import forms
from django.forms import ModelForm 

from .models import Submission

class SubmissionForm(forms.Form):
    """Form definition for Submission."""
    
    course_code = forms.CharField(max_length=20, required=True)
    assignment_code = forms.CharField( max_length=20, required=True)
    session_token = forms.CharField(max_length=20, required=True)
    reg_no = forms.CharField(max_length=20, required=True)
    assignment_file = forms.FileField( max_length=200, required=True)
    
    def __init__(self, *args, **kwargs):
        super(SubmissionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'