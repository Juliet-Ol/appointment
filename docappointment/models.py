from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    identiy_number = models.CharField(max_length=50, blank=True, primary_key=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=300, default='') 



