from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Cohort
from .serializers import CohortSerial

# Create your views here.

class CohortList(APIView):

    def get(self, reqest):
        cohort = Cohort.objects.all()
        serializer = CohortSerial(cohort, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CohortSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CohortDetails(APIView):
    
    def get_object(self, pk):
        try:
            return Cohort.objects.get(pk=pk)
        except Cohort.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        cohort = self.get_object(pk)
        serializer = CohortSerial(cohort)
        return Response(serializer.data)

    def put(self, request, pk):
        update_cohort = self.get_object(pk)
        serializer = CohortSerial(update_cohort, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_cohort = self.get_object(pk)
        delete_cohort.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


