from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Grades
from .serializers import GradesSerial

# Create your views here.

class GradesList(APIView):

    def get(self, reqest):
        grades = Grades.objects.all()
        serializer = GradesSerial(grades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GradesSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GradeDetails(APIView):
    
    def get_object(self, pk):
        try:
            return Grades.objects.get(pk=pk)
        except Grades.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        grades = self.get_object(pk)
        serializer = GradesSerial(grades)
        return Response(serializer.data)

    def put(self, request, pk):
        update_grades = self.get_object(pk)
        serializer = GradesSerial(update_grades, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_grades = self.get_object(pk)
        delete_grades.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

