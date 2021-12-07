from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Grades(models.Model):
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    assignment = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    grade = models.CharField( blank=True)
    comments = models.TextField(blank=True)

    
    

    def __str__(self):
        return self.name