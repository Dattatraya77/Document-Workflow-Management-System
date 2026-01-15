from django.db import models
from django.conf import settings


class Document(models.Model):
    STATUS_CHOICES = (
        ("DRAFT", "Draft"),
        ("IN_REVIEW", "In Review"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title