from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Seller(models.Model):
    username = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(default= "no bio...")
    pic = models.ImageField(upload_to='sellers', default = 'grey_skull.png')


    def __str__(self):
        return f"Profile of {self.username}"
