from rest_framework import serializers
from .models import Cohorts


class CohortSerial(serializers.ModelSerializer):
    class Meta:
        model = Cohorts

        fields = ('cohort_name','student')