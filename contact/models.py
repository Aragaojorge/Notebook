from django.db import models
from django.utils import timezone

# we need to import the module needed to create users
from django.contrib.auth.models import User

# Create your models here.

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)

# Creating the primary key
class Category(models.Model):
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

# Contact inherit from class Model
# class Contact holds data that will be persisted in the database
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) # black=true indicates that email field could be empty
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    # after include those 2 variables below was necessary to create new migrations
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )  
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'