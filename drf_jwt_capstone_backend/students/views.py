from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Students
from .serializers import StudentSerial

# Create your views here.

class StudentList(APIView):

    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerial(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetails(APIView):
    
    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerial(student)
        return Response(serializer.data)

    def put(self, request, pk):
        update_student = self.get_object(pk)
        serializer = StudentSerial(update_student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_student = self.get_object(pk)
        delete_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
