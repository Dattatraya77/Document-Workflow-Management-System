from django.db import models
from django.conf import settings


class AuditLog(models.Model):
    """
    Stores immutable audit records for document workflow actions.
    Used for compliance, debugging, and history tracking.
    """

    ACTION_CHOICES = (
        ("CREATED", "Created"),
        ("UPDATED", "Updated"),
        ("WORKFLOW_ASSIGNED", "Workflow Assigned"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs"
    )

    document_id = models.PositiveIntegerField(
        help_text="ID of the document on which the action was performed"
    )

    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES
    )

    comment = models.TextField(
        null=True,
        blank=True,
        help_text="Optional comment (e.g. rejection reason)"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"

    def __str__(self):
        return f"{self.action} | Document {self.document_id} | {self.created_at}"
