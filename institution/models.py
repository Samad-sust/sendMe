from django.db import models

# Create your models here.

# the following models don't have dependencies
class Institute(models.Model):
    """Model definition for Institute."""

    # TODO: Define fields here
    inst_name = models.CharField(max_length=100)
    inst_short_name = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Institution."""

        verbose_name = 'Institute'
        verbose_name_plural = 'Institute'

    def __str__(self):
        """Unicode representation of Institute."""
        return self.inst_name

# the following models don't have dependencies
class Department(models.Model):
    """Model definition for Department."""

    # TODO: Define fields here
    dept_name = models.CharField(max_length=100)
    dept_code = models.CharField( max_length=10)


    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        return self.dept_name

# the following models don't have dependencies
class Semester(models.Model):
    """Model definition for Semester."""

    # TODO: Define fields here
    sem_name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Semester."""

        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'

    def __str__(self):
        """Unicode representation of Semester."""
        return self.sem_name
