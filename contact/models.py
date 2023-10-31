from django.db import models
from django.utils import timezone
# Create your models here.

# Contact inherit from class Model
# class Contact holds data that will be persisted in the database
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) # black=true indicates that email field could be empty
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'