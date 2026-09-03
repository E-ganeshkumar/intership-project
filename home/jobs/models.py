from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    employer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=500)
    salary_min = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    salary_max = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table ='jobs'