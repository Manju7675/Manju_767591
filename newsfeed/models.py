from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    image=models.ImageField(upload_to='images')
    date=models.DateTimeField(auto_now_add=True)
    caption=models.TextField()
    userid = models.ForeignKey(User,on_delete=models.CASCADE)