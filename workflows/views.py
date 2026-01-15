# apps/workflows/views.py
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from .models import Workflow, WorkflowStep
from .serializers import (
    WorkflowCreateSerializer,
    WorkflowSerializer,
    WorkflowStepSerializer,
)


class WorkflowCreateAPIView(CreateAPIView):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowCreateSerializer
    permission_classes = [IsAdminUser]


class WorkflowDetailAPIView(RetrieveAPIView):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer
    permission_classes = [IsAuthenticated]


class WorkflowStepCreateAPIView(CreateAPIView):
    serializer_class = WorkflowStepSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        workflow = get_object_or_404(Workflow, pk=self.kwargs["pk"])
        serializer.save(workflow=workflow)
