from django.urls import path
from . import views

urlpatterns = [
    path('cohort/', views.CohortList.as_view),
    path('cohort/<int:pk>/', views.CohortDetails.as_view)
]