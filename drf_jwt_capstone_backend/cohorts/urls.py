from django.urls import path
from .views import CohortList, CohortDetails

urlpatterns = [
    path('cohorts/', CohortList.as_view(), name='all_cohorts'),
    path('cohorts/<int:pk>/', CohortDetails.as_view(), name='single_cohort')
]