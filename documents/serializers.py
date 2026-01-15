
from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Document
        fields = (
            "id",
            "title",
            "file",
            "status",
            "created_by",
            "created_at",
        )


class DocumentDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    workflow = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = (
            "id",
            "title",
            "file",
            "status",
            "created_by",
            "created_at",
            "workflow",
        )

    def get_workflow(self, obj):
        if hasattr(obj, "workflow_instance"):
            wf = obj.workflow_instance
            return {
                "workflow_name": wf.workflow.name,
                "current_step": wf.current_step,
            }
        return None
