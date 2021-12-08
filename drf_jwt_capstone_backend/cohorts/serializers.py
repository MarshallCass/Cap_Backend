from rest_framework import serializers
from .models import Cohort


class CohortSerial(serializers.ModelSerializer):
    class Meta:
        model = Cohort

        fields = ('cohort','student')