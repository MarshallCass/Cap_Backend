from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Assignments(models.Model):
    assignment_subject = models.CharField(max_length=50, blank=True)
    assignment_name = models.CharField(max_length=50, blank=True)
    assignment_description = models.TextField(blank=True)
    assignment_notes = models.TextField(blank=True)
    
    

    def __str__(self):
        return self.name