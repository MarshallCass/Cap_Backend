from django.urls import path
from . import views

urlpatterns = [
    path('assignments/', views.AssignmentList.as_view),
    path('assignments/<int:pk>/', views.ProjectDetails.as_view)
]