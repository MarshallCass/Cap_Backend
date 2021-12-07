from rest_framework import serializers
from .models import Assignments

class AssignmentsSerial(serializers.ModelSerializer):
    class Meta:
        model = Assignments

        fields = ('assignment_subject', 'assignment_name', 'assignment_description', 'assignment_notes')