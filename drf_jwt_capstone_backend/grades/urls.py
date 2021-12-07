from django.urls import path
from . import views

urlpatterns = [
    path('grades/', views.GradesList.as_view),
    path('grades/<int:pk>/', views.GradeDetails.as_view)
]