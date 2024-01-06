from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
