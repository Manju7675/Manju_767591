from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.BigIntegerField()
    gender=models.CharField(max_length=15)
    dob=models.DateField()