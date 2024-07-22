from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

