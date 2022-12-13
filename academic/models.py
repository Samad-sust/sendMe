from django.db import models

from institution.models import Semester, Department
from people.models import Teacher

# Create your models here.
class Course(models.Model):
    """Model definition for Course."""

    # TODO: Define fields here
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, verbose_name=("Course Teacher"))

    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        """Unicode representation of Course."""
        return self.course_name

class Assignment(models.Model):
    """Model definition for Assignment."""
    assignment_name = models.CharField(max_length=150)
    assignment_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_code = models.CharField(max_length=20, default="")
    assignment_active = models.BooleanField()


    class Meta:
        """Meta definition for Assignment."""

        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        """Unicode representation of Assignment."""
        return self.assignment_name
