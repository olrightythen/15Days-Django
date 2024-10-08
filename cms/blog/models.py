from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images' , blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

