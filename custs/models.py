# Create your models here.
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField(default='no notes')
    email = models.EmailField()
    pic = models.ImageField(upload_to='custs', default='grey_skull.png')


    def __str__(self):
        return str(self.name)
    
