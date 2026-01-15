
from django.db import models
from django.conf import settings

class Workflow(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkflowStep(models.Model):
    workflow = models.ForeignKey(
        Workflow,
        related_name="steps",
        on_delete=models.CASCADE
    )
    step_order = models.PositiveIntegerField()
    required_role = models.CharField(max_length=20)

    class Meta:
        ordering = ["step_order"]
        unique_together = ("workflow", "step_order")

    def __str__(self):
        return f"{self.workflow.name} - Step {self.step_order}"


class DocumentWorkflow(models.Model):
    """
    Tracks workflow execution state for a document
    """

    document = models.OneToOneField(
        "documents.Document",
        related_name="workflow_instance",
        on_delete=models.CASCADE
    )
    workflow = models.ForeignKey(
        Workflow,
        on_delete=models.CASCADE
    )
    current_step = models.PositiveIntegerField(default=1)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.document.title} - {self.workflow.name}"
