from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_detail.html'


class UserDetails(APIView):
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = RegistrationSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        update_user = self.get_object(pk)
        serializer = RegistrationSerializer(update_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_user = self.get_object(pk)
        delete_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    