from django.contrib import admin

# Register your models here.
from .models import Institute, Department, Semester

admin.site.register(Institute)
admin.site.register(Department)
admin.site.register(Semester)