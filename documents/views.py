# apps/documents/views.py
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Document
from .serializers import DocumentSerializer, DocumentDetailSerializer
from workflows.models import Workflow, DocumentWorkflow
from workflows.engine import WorkflowEngine


class DocumentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Document.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DocumentDetailSerializer
        return DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class MyDocumentsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        docs = Document.objects.filter(created_by=request.user)
        serializer = DocumentSerializer(docs, many=True)
        return Response(serializer.data)


class AssignWorkflowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        workflow_id = request.data.get("workflow_id")

        workflow = get_object_or_404(Workflow, pk=workflow_id)

        doc_workflow, created = DocumentWorkflow.objects.get_or_create(
            document=document,
            defaults={"workflow": workflow}
        )

        document.status = "IN_REVIEW"
        document.save()

        return Response({
            "message": "Workflow assigned",
            "current_step": doc_workflow.current_step
        })


class DocumentActionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, pk):
        action = request.data.get("action")
        doc_workflow = get_object_or_404(DocumentWorkflow, document_id=pk)

        WorkflowEngine.perform_action(
            user=request.user,
            document_workflow=doc_workflow,
            action=action
        )

        return Response({"message": f"Document {action} successful"})


class PendingDocumentsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        workflows = DocumentWorkflow.objects.filter(
            workflow__steps__required_role=request.user.role,
            document__status="IN_REVIEW"
        ).distinct()

        data = []
        for wf in workflows:
            data.append({
                "document_id": wf.document.id,
                "title": wf.document.title,
                "current_step": wf.current_step
            })

        return Response(data)


class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = Document.objects.filter(created_by=request.user)

        return Response({
            "draft": qs.filter(status="DRAFT").count(),
            "in_review": qs.filter(status="IN_REVIEW").count(),
            "approved": qs.filter(status="APPROVED").count(),
            "rejected": qs.filter(status="REJECTED").count(),
        })
