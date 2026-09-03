from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job


class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'APPLIED', 'Applied'
        SHORTLISTED = 'SHORTLISTED', 'Shortlisted'
        REJECTED = 'REJECTED', 'Rejected'
        HIRED = 'HIRED', 'Hired'

    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    candidate = models.ForeignKey(User,on_delete=models.CASCADE,related_name='applications')
    resume = models.URLField(blank=True,null=True)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.APPLIED)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['job', 'candidate'],
                name='unique_job_candidate_application'
            )
        ]

    class Meta:
        db_table = 'jobapplication'