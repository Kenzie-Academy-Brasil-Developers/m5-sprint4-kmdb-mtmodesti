
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from users.utils import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name','username']
    USERNAME_FIELD = "email"
    objects = CustomUserManager
