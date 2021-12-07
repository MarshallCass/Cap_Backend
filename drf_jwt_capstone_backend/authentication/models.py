from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    email = models.EmailField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    room_number = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)