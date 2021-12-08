from rest_framework import serializers
from .models import Students
from drf_jwt_capstone_backend.students.models import Students



class StudentSerial(serializers.ModelSerializer):
    class Meta:
        model = Students

        fields = ('first_name', 'last_name', 'address', 'zipcode', 
                  ' guardian_one', 'guardian_two')
