from django.db import models




# Create your models here.


class Grades(models.Model):
    student = models.ForeignKey('students.Students', null=True, on_delete=models.CASCADE)
    assignment = models.ForeignKey('assignments.Assignments', null=True, on_delete=models.CASCADE)
    grade = models.CharField( blank=True, max_length=5)
    comments = models.TextField(blank=True)
