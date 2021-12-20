from rest_framework import serializers
from .models import Students



class StudentSerial(serializers.ModelSerializer):
    class Meta:
        model = Students

        fields = ('first_name', 'last_name', 'address', 'zipcode', 
                  ' guardian_one', 'guardian_two')

def create(self, validated_data):

        student = Students.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            zipcode=validated_data['zipcode'],
            guardian_one=validated_data['guardian_one'],
            guardian_two=validated_data['guardian_two'],
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        student.save()

        return student
