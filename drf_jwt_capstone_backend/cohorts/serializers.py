from rest_framework import serializers
from .models import Cohort
from django.contrib.auth import get_user_model
User = get_user_model()

class CohortSerial(serializers.ModelSerializer):
    class Meta:
        model = Cohort

        fields = ('cohort','student')