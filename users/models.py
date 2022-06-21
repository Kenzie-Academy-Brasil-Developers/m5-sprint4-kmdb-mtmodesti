
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from users.utils import CustomUserManager

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=50)
    
    
    username = None
    
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
