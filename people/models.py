from django.db import models


from institution.models import Department, Institute

# Create your models here.
class Designation(models.Model):
    """Model definition for Designation."""

    # TODO: Define fields here
    desig_name = models.CharField(max_length=50)
    desig_short = models.CharField(max_length=10)

    class Meta:
        """Meta definition for Designation."""

        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'

    def __str__(self):
        """Unicode representation of Designation."""
        return self.desig_short

class Teacher(models.Model):
    """Model definition for Teacher."""
    
    teacher_name = models.CharField(max_length=50)
    teacher_desig = models.ForeignKey(Designation , on_delete=models.CASCADE)
    teacher_institution = models.ForeignKey(Institute, on_delete=models.CASCADE, null= True)
    teacher_dept = models.ForeignKey(Department, on_delete=models.CASCADE, null = True)

    class Meta:
        """Meta definition for Teacher."""

        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        """Unicode representation of Teacher."""
        return self.teacher_name
