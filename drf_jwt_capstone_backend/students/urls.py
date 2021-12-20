from django.urls import path
from .views import StudentList, StudentDetails

urlpatterns = [
    path('students/', StudentList.as_view(), name='all_students'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='single_student')
]