from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Cohort(models.Model):
    
    cohort_name = models.CharField(max_length=50, blank=True)
    student = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
       
    

    def __str__(self):
        return self.name