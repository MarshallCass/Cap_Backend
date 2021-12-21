from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'address', 'zipcode', 
                  'is_superuser', 'is_staff', 'is_parent', 'is_teacher', 'phone_number', 'room_number')

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            zipcode=validated_data['zipcode'],
            is_superuser=validated_data['is_superuser'],
            is_staff=validated_data['is_staff'],
            is_parent=validated_data['is_parent'],
            is_teacher=validated_data['is_teacher'],
            phone_number=validated_data['phone_number'],
            room_number=validated_data['room_number'],
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    
