# apps/workflows/urls.py
from django.urls import path
from .views import (
    WorkflowCreateAPIView,
    WorkflowDetailAPIView,
    WorkflowStepCreateAPIView,
)

urlpatterns = [
    path("", WorkflowCreateAPIView.as_view(), name="workflow-create"),
    path("<int:pk>/", WorkflowDetailAPIView.as_view(), name="workflow-detail"),
    path("<int:pk>/steps/", WorkflowStepCreateAPIView.as_view(), name="workflow-step-create"),
]
