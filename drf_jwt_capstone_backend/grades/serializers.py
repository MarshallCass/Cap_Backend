from rest_framework import serializers
from .models import Grades
from django.contrib.auth import get_user_model
User = get_user_model()

class GradesSerial(serializers.ModelSerializer):
    class Meta:
        model = Grades

        fields = ('student', 'assignment', 'grade', 'comments')