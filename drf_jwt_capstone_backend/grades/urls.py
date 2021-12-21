from django.urls import path
from .views import GradesList, GradeDetails

urlpatterns = [
    path('grades/', GradesList.as_view),
    path('grades/<int:pk>/', GradeDetails.as_view)
]