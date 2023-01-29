from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', login_required(views.SubmissionListView.as_view()), name="submission"),
    path('tokens/', login_required(views.SessionTokenListView.as_view()), name="session_token_list"),
]