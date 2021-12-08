from django.db import models
from drf_jwt_capstone_backend.students.models import Students



# Create your models here.


class Grades(models.Model):
    student = models.ForeignKey(Students, null=True, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Students, null=True, on_delete=models.CASCADE)
    grade = models.CharField( blank=True, max_length=5)
    comments = models.TextField(blank=True)
