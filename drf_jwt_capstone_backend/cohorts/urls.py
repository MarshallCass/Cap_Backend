from django.urls import path
from .views import CohortList, CohortDetails

urlpatterns = [
    path('cohort/', CohortList.as_view),
    path('cohort/<int:pk>/', CohortDetails.as_view)
]