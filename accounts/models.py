from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.utils import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(unique=False, null=True, max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updatedAt = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    objects = CustomUserManager()
