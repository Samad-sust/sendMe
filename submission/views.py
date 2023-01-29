from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from .models import Submission, SessionToken

# Create your views here.

class SubmissionListView(ListView):
    model = Submission
    template_name = "submission_list.html"
    ordering = ['-submission_date_time']

class SessionTokenListView(ListView):
    model = SessionToken
    template_name = "sess_tokens.html"
    context_object_name = 'tokens'
    ordering = ['-sessionToken_validity_time']

class SessionTokenCreateView(CreateView):
    model = SessionToken
    template_name = "create_sess_token.html"

class SessionTokenDetailView(DetailView):
    model = SessionToken
    template_name = "detail_sess_token.html"
