# apps/audit/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import AuditLog


class DocumentAuditLogAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, document_id):
        logs = AuditLog.objects.filter(document_id=document_id).order_by("-created_at")

        data = [
            {
                "user": log.user.username if log.user else None,
                "action": log.action,
                "timestamp": log.timestamp,
            }
            for log in logs
        ]

        return Response(data)
