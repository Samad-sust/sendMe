from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from root.filters import ListViewWithFilter
from .filters import SubmissionFilter, TokenFilter
from .models import Submission, SessionToken

# Create your views here.

class SubmissionListView(ListViewWithFilter):
    model = Submission
    target_filter = SubmissionFilter
    context_object_name = 'submission_list'
    template_name = "submission_list.html"
    ordering = ['-submission_date_time']

class SessionTokenListView(ListViewWithFilter):
    model = SessionToken
    target_filter = TokenFilter
    template_name = "sess_tokens.html"
    context_object_name = 'tokens'
    ordering = ['-sessionToken_validity_time']

# class BookListView(ListViewWithFilter):
#     model = Book
#     context_object_name = 'books'
#     target_filter = BookFilter
#     template_name = 'books.html'
#     paginate_by = 6


class SessionTokenCreateView(CreateView):
    model = SessionToken
    fields = ['sessionToken_token', 'sessionToken_validity_time' ,'sessionToken_expired']
    template_name = "create_sess_token.html"
    success_url = '/'
    

class SessionTokenDetailView(DetailView):
    model = SessionToken
    template_name = "detail_sess_token.html"
