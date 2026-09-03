from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userlogin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=12,unique=True,null=True)
    class Meta:
        db_table = 'users'