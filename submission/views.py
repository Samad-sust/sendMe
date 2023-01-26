from django.shortcuts import render
from django.views.generic import ListView

from .models import Submission

# Create your views here.

class SubmissionListView(ListView):
    model = Submission
    template_name = "submission_list.html"
