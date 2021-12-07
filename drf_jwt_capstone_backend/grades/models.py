from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Grades(models.Model):
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    assignment = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    grade = models.CharField( blank=True, max_length=5)
    comments = models.TextField(blank=True)
