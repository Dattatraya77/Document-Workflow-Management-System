
from rest_framework import serializers
from .models import Workflow, WorkflowStep, DocumentWorkflow


class WorkflowStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowStep
        fields = (
            "id",
            "step_order",
            "required_role",
        )


class WorkflowSerializer(serializers.ModelSerializer):
    steps = WorkflowStepSerializer(many=True, read_only=True)

    class Meta:
        model = Workflow
        fields = (
            "id",
            "name",
            "steps",
        )


class WorkflowCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = ("id", "name")


class DocumentWorkflowSerializer(serializers.ModelSerializer):
    document_title = serializers.CharField(
        source="document.title",
        read_only=True
    )
    workflow_name = serializers.CharField(
        source="workflow.name",
        read_only=True
    )

    class Meta:
        model = DocumentWorkflow
        fields = (
            "id",
            "document",
            "document_title",
            "workflow",
            "workflow_name",
            "current_step",
            "started_at",
            "completed_at",
        )
        read_only_fields = ("current_step",)
