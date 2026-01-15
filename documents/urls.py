# apps/documents/urls.py
from django.urls import path
from .views import (
    DocumentViewSet,
    MyDocumentsAPIView,
    AssignWorkflowAPIView,
    DocumentActionAPIView,
    PendingDocumentsAPIView,
    DashboardAPIView,
)

urlpatterns = [
    # Documents CRUD
    path("", DocumentViewSet.as_view({
        "get": "list",
        "post": "create"
    })),
    path("<int:pk>/", DocumentViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),

    # Custom APIs
    path("my/", MyDocumentsAPIView.as_view(), name="my-documents"),
    path("pending/", PendingDocumentsAPIView.as_view(), name="pending-documents"),
    path("dashboard/", DashboardAPIView.as_view(), name="dashboard"),

    # Workflow-related
    path("<int:pk>/assign-workflow/", AssignWorkflowAPIView.as_view(), name="assign-workflow"),
    path("<int:pk>/action/", DocumentActionAPIView.as_view(), name="document-action"),
]
