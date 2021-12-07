from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Assignments
from .serializers import AssignmentsSerial

# Create your views here.

class AssignmentList(APIView):

    def get(self, reqest):
        assignments = Assignments.objects.all()
        serializer = AssignmentsSerial(assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentsSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetails(APIView):
    
    def get_object(self, pk):
        try:
            return Assignments.objects.get(pk=pk)
        except Assignments.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        assignment = self.get_object(pk)
        serializer = AssignmentsSerial(reply)
        return Response(serializer.data)

    def put(self, request, pk):
        update_assignment = self.get_object(pk)
        serializer = AssignmentsSerial(update_assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_assignment = self.get_object(pk)
        delete_assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    