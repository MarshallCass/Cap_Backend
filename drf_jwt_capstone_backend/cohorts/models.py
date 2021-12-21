from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# from drf_jwt_capstone_backend.students.models import Students




# Create your models here.


class Cohorts(models.Model):
    
    cohort_name = models.CharField(max_length=50, blank=True)
    student = models.ForeignKey('students.Students', on_delete=models.CASCADE, blank=True, default= None)
       
    
