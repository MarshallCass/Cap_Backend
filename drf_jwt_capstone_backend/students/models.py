from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
User = get_user_model()


# Create your models here.


class Students(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    guardian_one = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    guardian_two = models.ForeignKey(User, null=True, on_delete=models.CASCADE)