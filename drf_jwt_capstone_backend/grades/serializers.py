from rest_framework import serializers
from .models import Grades


class GradesSerial(serializers.ModelSerializer):
    class Meta:
        model = Grades

        fields = ('student', 'assignment', 'grade', 'comments')