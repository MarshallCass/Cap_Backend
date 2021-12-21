from django.urls import path
from .views import GradesList, GradeDetails

urlpatterns = [
    path('grades/', GradesList.as_view(), name='all_grades'),
    path('grades/<int:pk>/', GradeDetails.as_view, name='single_grade')
]