from django.db import models

from datetime import datetime, timezone

from academic.models import Course, Assignment

# Create your models here.
class SessionToken(models.Model):
    """Model definition for SessionToken."""

    sessionToken_token = models.CharField(max_length=10)
    sessionToken_expired = models.BooleanField(default = False)
    sessionToken_validity_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        """Meta definition for SessionToken."""

        verbose_name = 'SessionToken'
        verbose_name_plural = 'SessionTokens'

    def __str__(self):
        """Unicode representation of SessionToken."""
        return self.sessionToken_token

def assin_sub_path(instance, filename):
     # file will be uploaded to MEDIA_ROOT/assignments/year/month

    x = datetime.now()

    crr_year = x.strftime("%Y")
    crr_mon = x.strftime("%B")
    return 'assignments/{0}/{1}/{2}/{3}/{4}'.format(instance.submission_course, instance.submission_assignment,
    crr_year, crr_mon, filename)

class Submission(models.Model):
    """Model definition for Submission."""

    submission_assignment = models.ForeignKey(Assignment , on_delete=models.CASCADE)
    submission_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    submission_date_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    submission_session_token = models.ForeignKey( SessionToken , on_delete=models.CASCADE)
    submission_reg_no = models.CharField(max_length=20)
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=False, null=True)
    user_agent = models.CharField(max_length=200, null=True, blank=True)
    submission_file = models.FileField(upload_to=assin_sub_path, max_length=100, null=True)


    class Meta:
        """Meta definition for Submission."""
        # unique_together = ['submission_course', 'submission_assignment']
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

    def __str__(self):
        """Unicode representation of Submission."""
        return self.submission_reg_no
