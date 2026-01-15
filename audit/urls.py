# apps/audit/urls.py
from django.urls import path
from .views import DocumentAuditLogAPIView

urlpatterns = [
    path("documents/<int:document_id>/", DocumentAuditLogAPIView.as_view(), name="document-audit"),
]
