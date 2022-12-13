from django.contrib import admin

from .models import SessionToken, Submission

# Register your models here.
admin.site.register(SessionToken)
admin.site.register(Submission)