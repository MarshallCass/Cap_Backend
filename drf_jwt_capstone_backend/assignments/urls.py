from django.urls import path
from .views import AssignmentList, ProjectDetails

urlpatterns = [
    path('assignments/', AssignmentList.as_view(), name='all_assignments'),
    path('assignments/<int:pk>/', ProjectDetails.as_view(), name='single_assignment')
]