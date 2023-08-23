from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField()
    email = models.EmailField()


    def __str__(self):
        return str(self.name)
    